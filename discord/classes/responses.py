"""
Response format classes
"""

from .user import AuthenticatedUser, GuildMember
from .presence import Presence

class GatewayReadyInfo:
	def __init__(self, data: dict) -> None:
		self.version = data['v']
		self.user_settings_proto = data['user_settings_proto']
		self.user_settings = data['user_settings']
		
		self.resume_gateway_url = data['resume_gateway_url']
		
		self.user = AuthenticatedUser(data['user'])
		
		self.notes = data['notes']
		self.relationships = data['relationships']
		self.presences = [Presence(presence_data) for presence_data in data['presences']]
		
		self.private_channels = data['private_channels']
		
		#self.channel_id = data['channel_id']
		#self.guild_id = data['guild_id']
		
		self.sessions = data['sessions']
		self.session_id = data['session_id']
		self.session_type = data['session_type']
		self.static_client_session_id = data['static_client_session_id']
		
		self.tutorial = data['tutorial']
		
		self._raw = data

class GuildMembersInfo:
	def __init__(self, data: dict) -> None:
		self.presences = None
		self.members = [GuildMember(user_data=user_data) for user_data in data['members']]
		self.not_found = data['not_found']
		
		self.guild_id = data['guild_id']
		self.chunk_index = data['chunk_index']
		self.chunk_count = data['chunk_count']
		
		self._raw = data
		
		presences_data = data.get('presences')
		
		if presences_data is not None:
			self.presences = [Presence(presence_data) for presence_data in presences_data]