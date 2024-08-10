from ..enums import ActivityType

class ActivityTimestamps:
	def __init__(self, data: dict) -> None:
		self.start = data.get('start')
		self.end = data.get('end')

class ActivityAssets:
	def __init__(self, data: dict = None) -> None:
		self.large_image = data.get('large_image')
		self.large_text = data.get('large_text')
		
		self.small_image = data.get('small_image')
		self.small_text = data.get('small_text')

class Activity:
	def __init__(self, data: dict) -> None:
		self.name = data['name']
		self.id = data['id']
		self.type = ActivityType(data['type'])
		
		self.timestamps = data.get('timestamps') and ActivityTimestamps(data['timestamps'])
		self.assets = ActivityAssets(data.get('assets', {}))
		
		self.state = data.get('state')
		self.details = data.get('details')
		self.application_id = data.get('application_id')
		self.buttons = data.get('buttons')
		
		self._raw = data
	
	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Activity):
			return False
		
		for key in self._raw.keys():
			if other._raw.get(key) != self._raw[key]:
				return False
		
		return True
	
	def __repr__(self) -> str:
		return f'<{self.__class__.__name__}: {self.type.name}, {self.name!r}, {self.state!r}>'