from ..utility.requester import Requester

from .gateway import DiscordGateway, GatewayEvent
from .channel import Channel
from .intents import Intents

class DiscordClient:
	def __init__(self, token: str, intents: Intents = None) -> None:
		self.token = token
		self.intents = intents
		
		self.requester = Requester(token=token)
		self.gateway = DiscordGateway.fromClient(self)
	
	def run(self):
		self.gateway.connect()
	
	def get_channel(self, channel_id: int):
		return Channel(self, channel_id)
	
	
	
	async def _on_event(self, event: GatewayEvent):
		data = event.data
	
	def on_message(self):
		pass
	
	def on_reaction_add(self, data):
		pass