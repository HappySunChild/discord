class BaseUser:
	def __init__(self, user_data: dict) -> None:
		self.id = int(user_data['id'])
	
	def __repr__(self) -> str:
		return f'<{self.__class__.__name__}: {self.id}>'

class User(BaseUser):
	def __init__(self, user_data: dict) -> None:
		super().__init__(user_data)
		
		self.display_name = user_data.get('global_name')
		self.username = user_data.get('username')
		self.discriminator = user_data.get('discriminator')

class AuthenticatedUser(BaseUser):
	def __init__(self, user_data: dict) -> None:
		super().__init__(user_data)
		
		self.verified = user_data.get('verified')
		self.nsfw_allowed = user_data.get('nsfw_allowed')
		self.mfa_enabled = user_data.get('mfa_enabled')
		self.email = user_data.get('email')

class GuildMember:
	def __init__(self, user_data: dict) -> None:
		self.user = User(user_data['user'])
		
		self.roles = user_data['roles']
		self.joined_at = user_data['joined_at']
		self.mute = user_data['mute']
		self.deaf = user_data['deaf']