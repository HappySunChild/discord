from ..utility.requester import Requester
from ..enums import GatewayEventType

from .gateway import DiscordGateway, GatewayEvent
from .text.channel import Channel
from .intents import Intents

from .user import AuthenticatedUser
from .presence import Presence
from .responses import GatewayReadyInfo, GuildMembersInfo

import asyncio

class DiscordClient:
	def __init__(self, token: str, intents: Intents = None) -> None:
		self._ready = False
		
		self.token = token
		self.intents = intents
		
		self.requester = Requester(token=token)
		self.gateway = DiscordGateway.fromClient(self)
	
	async def wait_for_ready(self):
		while not self._ready:
			await asyncio.sleep(0)
	
	def run(self):
		self.gateway.start()
	
	async def run_async(self):
		await self.gateway._start()
	
	async def close(self):
		await self.gateway._disconnect()
	
	
	def get_channel(self, channel_id: int):
		return Channel(self, channel_id)
	
	def get_authenticated_user(self):
		user_data, _ = self.requester.get(
			url='https://discord.com/api/v9/users/@me'
		)
		
		return AuthenticatedUser(user_data=user_data)
	
	async def request_get_guild_members(self, guild_id: int, limit: int = 0, query: str = None, user_ids: list[int] = None, presences: bool = False):
		await self.gateway.request_get_guild_members(guild_id=guild_id, limit=limit, query=query, user_ids=user_ids, presences=presences)
	
	
	async def _on_event(self, event: GatewayEvent):
		event_type = event.type
		data: dict = event.data
		
		if event_type == GatewayEventType.Ready:
			await self._on_ready(GatewayReadyInfo(data=data))
		elif event_type == GatewayEventType.GuildMembersChunk:
			await self.on_guild_members_response(GuildMembersInfo(data=data))
		elif event_type == GatewayEventType.MessageCreate:
			await self.on_message(data)
		elif event_type == GatewayEventType.MessageReactionAdd:
			await self.on_reaction_add(data)
		elif event_type == GatewayEventType.PresenceUpdate:
			await self.on_presence_update(Presence(data))
	
	async def _on_ready(self, info: GatewayReadyInfo):
		self._ready = True
		await self.on_ready(info=info)
	
	# events
	async def on_ready(self, info: GatewayReadyInfo):
		pass
	
	async def on_presence_update(self, presence: Presence):
		pass
	
	async def on_message(self, data):
		pass
	
	async def on_reaction_add(self, data):
		pass
	
	async def on_guild_members_response(self, info: GuildMembersInfo):
		pass
	
	def __repr__(self) -> str:
		return f'<{self.__class__.__name__} {self.token}>'