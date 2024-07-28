from enum import Enum

class GatewayEventType(Enum):
	Default = None
	Ready = 'READY'
	
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
	
	MessageCreate = 'MESSAGE_CREATE'
	MessageUpdate = 'MESSAGE_UPDATE'
	MessageDelete = 'MESSAGE_DELETE'
	MessageDeleteBulk = 'MESSAGE_DELETE_BULK'
	
	MessageReactionAdd = 'MESSAGE_REACTION_ADD'
	MessageReactionRemove = 'MESSAGE_REACTION_REMOVE'
	MessageReactionRemoveAll = 'MESSAGE_REACTION_REMOVE_ALL'
	MessageReactionRemoveEmoji = 'MESSAGE_REACTION_REMOVE_EMOJI'
	
	TypingStart = 'TYPING_START'