from __future__ import annotations
from typing import Optional, Any, TYPE_CHECKING

from socket2 import WebsocketClient, WebsocketResponse
from ..enums import GatewayEventType, GatewayOperation

from ..exceptions import HeartbeatNotAcknowledged

from sys import platform
from time import perf_counter
import asyncio

if TYPE_CHECKING:
	from .client import DiscordClient

class HeartbeatHandler:
	def __init__(self, gateway: DiscordGateway, interval: int) -> None:
		self.gateway = gateway
		
		self.interval = interval / 1000
		self._last_ack = perf_counter()
		self._sleep_task = None
	
	async def start(self):
		while self.gateway.is_connected:
			if self._last_ack + 60 < perf_counter():
				raise HeartbeatNotAcknowledged('Heartbeat did not receive a HeartbeatACK response')
			
			await self.beat()
			
			self._sleep_task = asyncio.create_task(self.sleep_interval())
			await self._sleep_task
	
	async def sleep_interval(self):
		try:
			await asyncio.sleep(self.interval)
		except asyncio.CancelledError:
			pass # don't really care if this gets cancelled
	
	async def beat(self):
		await self.gateway._send(operation=GatewayOperation.Heartbeat, payload=self.gateway._sequence)
	
	def acknowledge(self):
		self._last_ack = perf_counter()
	
	def stop(self):
		self._sleep_task.cancel()

class EventHandler:
	def __init__(self, gateway: DiscordGateway) -> None:
		self.gateway = gateway
	
	async def run_event(self):
		gateway = self.gateway
		event = await gateway._receive()
		
		if gateway.heartbeats:
			if event.operation == GatewayOperation.HeartbeatAcknowledged:
				gateway.heartbeats.acknowledge()
				
				return
			elif event.operation == GatewayOperation.Heartbeat:
				gateway.heartbeats.beat()
				
				return
		
		await gateway.on_event(event=event)
	
	async def start(self):
		while self.gateway.is_connected:
			await self.run_event()


class GatewayEvent:
	def __init__(self, response: WebsocketResponse) -> None:
		data: dict = response.json
		
		self.data = data['d']
		self.sequence = data['s']
		self.operation = data['op']
		self.type = GatewayEventType(data['t'])
	
	def __repr__(self) -> str:
		return f'<{self.__class__.__name__}: {self.type} ({self.operation})>'

class DiscordGateway:
	def __init__(self, token: str, intents = None) -> None:
		self.socket = WebsocketClient('wss://gateway.discord.gg')
		self.token = token
		self.intents = intents
		
		self.heartbeats: Optional[HeartbeatHandler] = None
		self.events: Optional[EventHandler] = None
		self._sequence = None
	
	@classmethod
	def fromClient(cls, client: DiscordClient):
		token = client.token
		
		new_gateway = cls(token=token, intents=client.intents)
		new_gateway.on_event = client._on_event
		
		return new_gateway
	
	@property
	def is_connected(self):
		return self.socket.is_connected
	
	
	def start(self):
		"""
		Starts a asynchronous process to handle gateway events
		"""
		
		asyncio.run(self._start())
	
	async def on_event(self, event: GatewayEvent):
		pass
	
	async def _start(self):
		"""
		Connects to discord's websocket gateway
		"""
		
		await self.socket._connect() # connect
		await self._perform_handshake() # handshake
		
		# start event handler and heartbeat
		await asyncio.gather(self.events.start(), self.heartbeats.start())
	
	async def _disconnect(self):
		self.heartbeats.stop()
		
		await self.socket._disconnect()
	
	async def _perform_handshake(self):
		"""
		Performs handshake with discord's gateway
		"""
		
		hello_event = await self._receive()
		
		interval = hello_event.data['heartbeat_interval']
		
		self.events = EventHandler(gateway=self)
		self.heartbeats = HeartbeatHandler(gateway=self, interval=interval)
		
		await self.heartbeats.beat()
		await self._send_identity()
	
	
	async def request_get_guild_members(self, guild_id: int, limit: int = 0, query: str = None, user_ids: list[int] = None, presences: bool = False):
		payload = {
			'guild_id': guild_id,
			'query': query,
			'limit': limit,
			
			'presences': presences,
			'user_ids': user_ids
		}
		
		await self._send(operation=GatewayOperation.RequestGuildMembers, payload=payload)
	
	
	async def _send_identity(self):
		payload = {
			'token': self.token,
			'properties': {
				'os': platform,
				'browser': 'python',
				'device': 'python'
			}
		}
		
		if self.intents:
			payload['intents'] = int(self.intents)
		
		await self._send(GatewayOperation.Identify, payload)
	
	async def _send(self, operation: int, payload: Any = None):
		await self.socket.send({
			'op': operation,
			'd': payload
		})
	
	async def _receive(self):
		if not self.is_connected:
			return
		
		response = await self.socket.receive()
		
		return GatewayEvent(response=response)