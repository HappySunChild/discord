from .user import BaseUser
from ..enums import PresenceStatusType

from .activity import Activity, ActivityType

class Presence:
	def __init__(self, presence_data: dict) -> None:
		self.status = PresenceStatusType(presence_data['status'])
		self.client_status = presence_data['client_status']
		
		self.activities = [Activity(data) for data in presence_data['activities']]
		
		self.user = BaseUser(presence_data['user'])
		self._raw = presence_data
	
	def has_activity(self, activity_type: ActivityType):
		for activity in self.activities:
			if activity.type == activity_type:
				return True
		
		return False
	
	def __repr__(self) -> str:
		return f'<{self.__class__.__name__}: {self.user}, {self.status}>'