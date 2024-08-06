from __future__ import annotations
from typing import TYPE_CHECKING

from .embed import Embed
from ..user import User

if TYPE_CHECKING:
	from ..webhook import Webhook

class Message:
	def __init__(self, message_data: dict) -> None:
		self.id = message_data['id']
		self.channel_id = message_data['channel_id']
		
		self.content = message_data['content']
		self.embeds = [Embed(**embed_data) for embed_data in message_data['embeds']]
		
		self.mentions = message_data['mentions']
		
		self.timestamp = message_data['timestamp']
		self.edited_timestamp = message_data.get('edited_timestamp')
		
		self.author = User(message_data['author'])
	
	def __repr__(self) -> str:
		return f'<{self.__class__.__name__}: {self.content}, {self.author}>'

class WebhookMessage(Message):
	def __init__(self, webhook: Webhook, message_data: dict) -> None:
		super().__init__(message_data)
		
		self.webhook = webhook
	
	def edit(self, message: str, *embeds: Embed):
		self.webhook.edit(self.id, message, *embeds)
		
		self.content = message
		self.embeds = embeds
	
	def delete(self):
		self.webhook.delete(self.id)