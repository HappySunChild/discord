from ..enums import ActivityType

class ActivityTimestamps:
	def __init__(self, data: dict) -> None:
		self.start = data.get('start')
		self.end = data.get('end')

class Activity:
	def __init__(self, data: dict) -> None:
		self.name = data['name']
		self.id = data['id']
		self.type = ActivityType(data['type'])
		
		self.timestamps = data.get('timestamps') and ActivityTimestamps(data['timestamps'])
		
		self.state = data.get('state')
		self.details = data.get('details')
		self.application_id = data.get('application_id')
		self.buttons = data.get('buttons')
		self.assets = data.get('assets')
		
		self._raw = data
	
	def __repr__(self) -> str:
		return f'<{self.__class__.__name__}: {self.type.name}, {self.name!r}, {self.state!r}>'