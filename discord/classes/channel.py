from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseItem

if TYPE_CHECKING:
	from .client import DiscordClient

class Channel(BaseItem):
	def __init__(self, client: DiscordClient, id: int) -> None:
		super().__init__(client, id)
	
	def send_message(self, message: str):
		
		payload = {
			'content': message,
		}
		
		_, res = self.client.requester.post(
			url=f'https://discord.com/api/v9/channels/{self.id}/messages',
			json=payload
		)
		
		print(res, res.json())