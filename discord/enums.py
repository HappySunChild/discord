from enum import Enum, IntEnum

class GatewayOperation(IntEnum):
	Heartbeat = 1 				# send/receive
	HeartbeatAcknowledged = 11 	# receive
	
	Hello = 10 					# receive
	Identify = 2 				# send
	Dispatch = 0 				# receive
	
	PresenceUpdate = 3 			# send
	VoiceStateUpdate = 4 		# send
	Resume = 6 					# send
	Reconnect = 7 				# receive
	RequestGuildMembers = 8 	# send
	InvalidSession = 9 			# receive

class GatewayEventType(Enum):
	Unknown = None
	
	Ready = 'READY'
	SessionsReplace = 'SESSIONS_REPLACE'
	
	GuildCreate = 'GUILD_CREATE'
	GuildUpdate = 'GUILD_UPDATE'
	GuildDelete = 'GUILD_DELETE'
	
	GuildRoleCreate = 'GUILD_ROLE_CREATE'
	GuildRoleUpdate = 'GUILD_ROLE_UPDATE'
	GuildRoleDelete = 'GUILD_ROLE_DELETE'
	
	ChannelCreate = 'CHANNEL_CREATE'
	ChannelUpdate = 'CHANNEL_UPDATE'
	ChannelDelete = 'CHANNEL_DELETE'
	ChannelPinsUpdate = 'CHANNEL_PINS_UPDATE'
	
	ThreadCreate = 'THREAD_CREATE'
	ThreadUpdate = 'THREAD_UPDATE'
	ThreadDelete = 'THREAD_DELETE'
	ThreadListSync = 'THREAD_LIST_SYNC'
	ThreadMemberUpdate = 'THREAD_MEMBER_UPDATE'
	ThreadMembersUpdate = 'THREAD_MEMBERS_UPDATE'
	
	StageInstanceCreate = 'STAGE_INSTANCE_CREATE'
	StageInstanceUpdate = 'STAGE_INSTANCE_UPDATE'
	StageInstanceDelete = 'STAGE_INSTANCE_DELETE'
	
	GuildMemberAdd = 'GUILD_MEMBER_ADD'
	GuildMemberUpdate = 'GUILD_MEMBER_UPDATE'
	GuildMemberRemove = 'GUILD_MEMBER_REMOVE'
	
	GuildAuditLogEntryCreate = 'GUILD_AUDIT_LOG_ENTRY_CREATE'
	GuildBanAdd = 'GUILD_BAN_ADD'
	GuildBanRemove = 'GUILD_BAN_REMOVE'
	
	GuildEmojisUpdate = 'GUILD_EMOJIS_UPDATE'
	GuildStickersUpdate = 'GUILD_STICKERS_UPDATE'
	
	GuildIntegrationsUpdate = 'GUILD_INTEGRATIONS_UPDATE'
	IntegrationCreate = 'INTEGRATION_CREATE'
	IntegrationUpdate = 'INTEGRATION_UPDATE'
	IntegrationDelete = 'INTEGRATION_DELETE'
	
	WebhooksUpdate = 'WEBHOOKS_UPDATES'
	
	InviteCreate = 'INVITE_CREATE'
	InviteDelete = 'INVITE_DELETE'
	
	VoiceStateUpdate = 'VOICE_STATE_UPDATE'
	VoiceChannelStatusUpdate = 'VOICE_CHANNEL_STATUS_UPDATE'
	
	PresenceUpdate = 'PRESENCE_UPDATE'
	
	ConversationSummaryUpdate = 'CONVERSATION_SUMMARY_UPDATE'
	MessageCreate = 'MESSAGE_CREATE'
	MessageUpdate = 'MESSAGE_UPDATE'
	MessageDelete = 'MESSAGE_DELETE'
	MessageDeleteBulk = 'MESSAGE_DELETE_BULK'
	MessageAcknowledge = 'MESSAGE_ACK'
	
	MessageReactionAdd = 'MESSAGE_REACTION_ADD'
	MessageReactionRemove = 'MESSAGE_REACTION_REMOVE'
	MessageReactionRemoveAll = 'MESSAGE_REACTION_REMOVE_ALL'
	MessageReactionRemoveEmoji = 'MESSAGE_REACTION_REMOVE_EMOJI'
	
	RelationshipAdd = 'RELATIONSHIP_ADD'
	RelationshipRemove = 'RELATIONSHIP_REMOVE'
	
	NotificationCreate = 'NOTIFICATION_CENTER_ITEM_CREATE'
	
	TypingStart = 'TYPING_START'