from ..utility.requester import Requester
from ..enums import GatewayEventType

from .gateway import DiscordGateway, GatewayEvent
from .text.channel import Channel
from .intents import Intents

from .presence import Presence
from .responses import GatewayReadyInfo, GuildMembersInfo

class DiscordClient:
	def __init__(self, token: str, intents: Intents = None) -> None:
		self.token = token
		self.intents = intents
		
		self.requester = Requester(token=token)
		self.gateway = DiscordGateway.fromClient(self)
	
	def run(self):
		self.gateway.start()
	
	async def close(self):
		await self.gateway._disconnect()
	
	
	def get_channel(self, channel_id: int):
		return Channel(self, channel_id)
	
	async def request_get_guild_members(self, guild_id: int, limit: int = 0, query: str = None, user_ids: list[int] = None, presences: bool = False):
		await self.gateway.request_get_guild_members(guild_id=guild_id, limit=limit, query=query, user_ids=user_ids, presences=presences)
	
	
	async def _on_event(self, event: GatewayEvent):
		event_type = event.type
		data: dict = event.data
		
		if event_type == GatewayEventType.Ready:
			await self.on_ready(GatewayReadyInfo(data=data))
		elif event_type == GatewayEventType.GuildMembersChunk:
			await self.on_guild_members_response(GuildMembersInfo(data=data))
		elif event_type == GatewayEventType.MessageCreate:
			await self.on_message(data)
		elif event_type == GatewayEventType.MessageReactionAdd:
			await self.on_reaction_add(data)
		elif event_type == GatewayEventType.PresenceUpdate:
			await self.on_presence_update(Presence(data))
	
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