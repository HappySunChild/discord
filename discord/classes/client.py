from .gateway import DiscordGateway, GatewayEvent

class DiscordClient:
	def __init__(self, token: str) -> None:
		self.token = token
		self.gateway = DiscordGateway.fromClient(self)
	
	async def _on_event(self, event: GatewayEvent):
		data = event.data
	
	def run(self):
		print('start client')
		self.gateway.connect()
	
	def send_message(self, data):
		pass
	
	def on_reaction_add(self, data):
		pass