class Intents:
	FLAGS = [
		'Guilds',
		
		'GuildMembers',
		'GuildModeration',
		'GuildEmojisAndStickers',
		'GuildIntergrations',
		'GuildWebhooks',
		'GuildInvites',
		'GuildVoiceStates',
		'GuildPresences',
		
		'GuildMessages',
		'GuildMessagesReactions',
		'GuildMessagesTyping',
		
		'DirectMessages',
		'DirectMessagesReactions',
		'DirectMessagesTyping'
		
		'MessageContent'
	]
	
	@classmethod
	def default(cls):
		new_intents = cls()
		new_intents.DirectMessages = True
		new_intents.DirectMessagesReactions = True
		new_intents.DirectMessagesTyping = True
		
		new_intents.GuildMessages = True
		new_intents.GuildMessagesReactions = True
		new_intents.GuildMessagesTyping = True
		
		return new_intents
	
	def __init__(self) -> None:
		for index, attr in enumerate(self.FLAGS):
			setattr(self, attr, False)
	
	def __int__(self):
		flag_value = 0
		
		for index, attr in enumerate(self.FLAGS):
			if getattr(self, attr):
				flag_value += 1 << index
		
		return flag_value