from __future__ import annotations
from typing import TYPE_CHECKING

from .message import Message

if TYPE_CHECKING:
	from ..client import DiscordClient

class Channel:
	def __init__(self, client: DiscordClient, id: int) -> None:
		self.client = client
		self.id = id
	
	def get_messages(self, limit: int = 50, before: int = None):
		messages_data, _ =self.client.requester.get(
			url=f'https://discord.com/api/v9/channels/{self.id}/messages',
			params={
				'limit': limit,
				'before': before
			}
		)
		
		return [
			Message(message_data=message_data)
			for message_data in messages_data
		]
	
	def send_message(self, message: str):
		payload = {
			'content': message,
		}
		
		self.client.requester.post(
			url=f'https://discord.com/api/v9/channels/{self.id}/messages',
			json=payload
		)