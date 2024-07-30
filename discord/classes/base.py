from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ..client import DiscordClient

class BaseItem:
	client = None
	id = None
	
	def __init__(self, client: DiscordClient, id: int) -> None:
		self.client = client
		self.id = id
	
	def __repr__(self) -> str:
		return f'<{self.__class__.__name__}: {self.id}>'
	
	def __int__(self):
		return self.id or -1