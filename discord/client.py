from .utility.requester import Requester

from .classes.gateway import DiscordGateway, GatewayEvent
from .classes.channel import Channel
from .classes.intents import Intents

class DiscordClient:
	def __init__(self, token: str, intents: Intents = None) -> None:
		self.token = token
		self.intents = intents
		
		self.requester = Requester(token=token)
		self.gateway = DiscordGateway.fromClient(self)
	
	def run(self):
		print('start client')
		self.gateway.connect()
	
	def get_channel(self, channel_id: int):
		return Channel(self, channel_id)
	
	
	
	async def _on_event(self, event: GatewayEvent):
		data = event.data
	
	def on_reaction_add(self, data):
		pass