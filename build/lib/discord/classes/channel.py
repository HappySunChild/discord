from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .client import DiscordClient

class Channel:
	def __init__(self, client: DiscordClient, id: int) -> None:
		self.client = client
		self.id = id
	
	def send_message(self, message: str):
		payload = {
			'content': message,
		}
		
		_, res = self.client.requester.post(
			url=f'https://discord.com/api/v9/channels/{self.id}/messages',
			json=payload
		)
		
		print(res, res.json())