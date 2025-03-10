from ..utility.requester import Requester

from .text.message import WebhookMessage
from .text.embed import Embed

class WebhookRequester(Requester):
	def process_url(self, url: str) -> str:
		return f'{url}?wait=true'

class Webhook:
	def __init__(self, id: int, token: str) -> None:
		self.id = id
		self.token = token
		
		self.name = None
		self.avatar_url = None
		
		self.requester = WebhookRequester()
	
	@property
	def url(self):
		return f'https://discord.com/api/webhooks/{self.id}/{self.token}'
	
	def _get_data(self):
		data = {
			'username': self.name,
			'avatar_url': self.avatar_url,
			'content': ''
		}
		
		return data
	
	
	def create_embed(self, title: str, description: str = None):
		return Embed(title=title, description=description)
	
	
	def delete(self, message_id: int):
		self.requester.delete(f'{self.url}/messages/{message_id}')
	
	def edit(self, message_id: int, message: str, *embeds: Embed):
		data = self._get_data()
		data['content'] = message
		data['embeds'] = [embed._get_data() for embed in embeds]
		
		self.requester.patch(f'{self.url}/messages/{message_id}', data)
	
	def send(self, message: str, *embeds: Embed):
		data = self._get_data()
		data['content'] = message
		data['embeds'] = [embed._get_data() for embed in embeds]
		
		message_data, _ = self.requester.post(self.url, data)
		
		return WebhookMessage(self, message_data)
	
	def set_avatar(self, avatarUrl: str):
		self.avatar_url = avatarUrl
	
	def set_name(self, newName: str):
		self.name = newName