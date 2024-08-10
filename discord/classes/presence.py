from .user import BaseUser
from ..enums import PresenceStatusType

from .activity import Activity, ActivityType

class ClientStatus:
	def __init__(self, status_data: dict) -> None:
		self.desktop_presence = PresenceStatusType(status_data.get('desktop', 'offline'))
		self.web_presence = PresenceStatusType(status_data.get('web', 'offline'))
		self.mobile_presence = PresenceStatusType(status_data.get('mobile', 'offline'))
		
		self.platforms = list(status_data.keys())
		
		self._raw = status_data
	
	@property
	def is_web(self):
		return self.web_presence != PresenceStatusType.Offline
	
	@property
	def is_desktop(self):
		return self.desktop_presence != PresenceStatusType.Offline
	
	@property
	def is_mobile(self):
		return self.mobile_presence != PresenceStatusType.Offline

PRESENCE_COLORS = {
	'Online': 0x23A55A,
	'Idle': 0xF0B232,
	'DoNotDisturb': 0xF23F43,
	'Offline': 0x80848E
}

class Presence:
	def __init__(self, presence_data: dict) -> None:
		self.status = PresenceStatusType(presence_data['status'])
		self.client_status = ClientStatus(presence_data['client_status'])
		
		self.activities = [Activity(data) for data in presence_data['activities']]
		
		self.user = BaseUser(presence_data['user'])
		self._raw = presence_data
	
	@property
	def color(self):
		return PRESENCE_COLORS[self.status.name]
	
	@property
	def in_voice_chat(self):
		return self.has_activity(ActivityType.HangStatus)
	
	def has_activity(self, activity_type: ActivityType):
		for activity in self.activities:
			if activity.type == activity_type:
				return True
		
		return False
	
	def __repr__(self) -> str:
		return f'<{self.__class__.__name__}: {self.user}, {self.status}>'