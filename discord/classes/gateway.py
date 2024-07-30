from __future__ import annotations
from typing import Any, TYPE_CHECKING

from socket2 import WebsocketClient, WebsocketResponse
from ..enums import GatewayEventType, GatewayOperation
from ..exceptions import HeartbeatNotAcknowledged

from sys import platform
from asyncio import run, sleep, gather

if TYPE_CHECKING:
	from .client import DiscordClient

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
	def __init__(self, token: str) -> None:
		self.socket = WebsocketClient('wss://gateway.discord.gg')
		self.token = token
		
		self._last_sequence = None
		self._heartbeat_interval = None
	
	@classmethod
	def fromClient(cls, client: DiscordClient):
		token = client.token
		
		new_gateway = cls(token=token)
		new_gateway.on_event = client._on_event
		
		return new_gateway
	
	def connect(self):
		run(self._connect())
	
	async def on_event(self, event: GatewayEvent):
		pass
	
	async def _connect(self):
		await self.socket._connect()
		await self._handshake()
		
		await gather(self._event_loop(), self._hearbeat_loop())
	
	async def _handshake(self):
		"""
		Performs handshake with discord's gateway
		"""
		
		hello_event = await self._receive()
		
		self._heartbeat_interval = hello_event.data['heartbeat_interval']
		
		await self._send_heartbeat()
		await self._send_identity()
	
	
	async def _event_loop(self):
		while True:
			event = await self._receive()
			
			if event.operation == GatewayOperation.Heartbeat:
				await self._send_heartbeat()
				
				continue
			
			await self.on_event(event=event)
	
	async def _hearbeat_loop(self):
		while True:
			await sleep(self._heartbeat_interval)
			await self._send_heartbeat()
	
	
	async def _send_heartbeat(self):
		await self._send(operation=1, payload=self._heartbeat_interval)
		
		heartbeat_res = await self._receive()
		
		if heartbeat_res.operation != GatewayOperation.HeartbeatAcknowledged:
			raise HeartbeatNotAcknowledged('Heartbeat did not receive a HeartbeatACK response')
	
	async def _send_identity(self):
		await self._send(2, {
			'token': self.token,
			'properties': {
				'os': platform,
				'browser': 'python',
				'device': 'python'
			}
		})
	
	async def _send(self, operation: int, payload: Any = None):
		await self.socket.send({
			'op': operation,
			'd': payload
		})
	
	async def _receive(self):
		response = await self.socket.receive()
		
		return GatewayEvent(response=response)