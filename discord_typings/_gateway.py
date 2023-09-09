from typing import (
    Any, Dict, Generic, List, Mapping, Optional, Tuple, TypeVar, Union
)

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import discord_typings

__all__ = (
    'GetGatewayData',
    'GetGatewayBotData',
    'SessionStartLimitData',
    'IdentifyData',
    'IdentifyConnectionPropertiesData',
    'IdentifyCommand',
    'ResumeData',
    'ResumeCommand',
    'HeartbeatCommand',
    'RequestGuildMembersData',
    'RequestGuildMembersCommand',
    'UpdateVoiceStateData',
    'UpdateVoiceStateCommand',
    'UpdatePresenceData',
    'UpdatePresenceCommand',
    'HelloData',
    'HelloEvent',
    'HeartbeatACKEvent',
    'PartialApplicationData',
    'ReadyData',
    'ReadyEvent',
    'ResumedData',
    'ResumedEvent',
    'ReconnectEvent',
    'InvalidSessionEvent',
    'ApplicationCommandPermissionsUpdateData',
    'ApplicationCommandPermissionsUpdateEvent',
    'AutoModerationRuleCreateData',
    'AutoModerationRuleCreateEvent',
    'AutoModerationRuleUpdateData',
    'AutoModerationRuleUpdateEvent',
    'AutoModerationRuleDeleteData',
    'AutoModerationRuleDeleteEvent',
    'AutoModerationActionExecutionData',
    'AutoModerationActionExecutionEvent',
    'ChannelCreateData',
    'ChannelCreateEvent',
    'ChannelUpdateData',
    'ChannelUpdateEvent',
    'ChannelDeleteData',
    'ChannelDeleteEvent',
    'ThreadCreateData',
    'ThreadCreateEvent',
    'ThreadUpdateData',
    'ThreadUpdateEvent',
    'ThreadDeleteData',
    'ThreadDeleteEvent',
    'ThreadListSyncData',
    'ThreadListSyncEvent',
    'ThreadMemberUpdateData',
    'ThreadMemberUpdateEvent',
    'ThreadMembersUpdateData',
    'ThreadMembersUpdateEvent',
    'ChannelPinsUpdateData',
    'ChannelPinsUpdateEvent',
    'GuildCreateData',
    'GuildCreateEvent',
    'GuildUpdateData',
    'GuildUpdateEvent',
    'GuildDeleteData',
    'GuildDeleteEvent',
    'GuildAuditLogEntryCreateData',
    'GuildAuditLogEntryCreateEvent',
    'GuildBanAddData',
    'GuildBanAddEvent',
    'GuildBanRemoveData',
    'GuildBanRemoveEvent',
    'GuildEmojisUpdateData',
    'GuildEmojisUpdateEvent',
    'GuildStickersUpdateData',
    'GuildStickersUpdateEvent',
    'GuildIntergrationsUpdateData',
    'GuildIntergrationsUpdateEvent',
    'GuildMemberAddData',
    'GuildMemberAddEvent',
    'GuildMemberRemoveData',
    'GuildMemberRemoveEvent',
    'GuildMemberUpdateData',
    'GuildMemberUpdateEvent',
    'GuildMembersChunkData',
    'GuildMembersChunkEvent',
    'GuildRoleCreateData',
    'GuildRoleCreateEvent',
    'GuildRoleUpdateData',
    'GuildRoleUpdateEvent',
    'GuildRoleDeleteData',
    'GuildRoleDeleteEvent',
    'GuildScheduledEventCreateData',
    'GuildScheduledEventCreateEvent',
    'GuildScheduledEventUpdateData',
    'GuildScheduledEventUpdateEvent',
    'GuildScheduledEventDeleteData',
    'GuildScheduledEventDeleteEvent',
    'GuildScheduledEventUserAddData',
    'GuildScheduledEventUserAddEvent',
    'GuildScheduledEventUserRemoveData',
    'GuildScheduledEventUserRemoveEvent',
    'IntegrationCreateData',
    'IntegrationCreateEvent',
    'IntegrationUpdateData',
    'IntegrationUpdateEvent',
    'IntegrationDeleteData',
    'IntegrationDeleteEvent',
    'InviteCreateData',
    'InviteCreateEvent',
    'InviteDeleteData',
    'InviteDeleteEvent',
    'MessageCreateData',
    'MessageCreateEvent',
    'MessageUpdateData',
    'MessageUpdateEvent',
    'MessageDeleteData',
    'MessageDeleteEvent',
    'MessageDeleteBulkData',
    'MessageDeleteBulkEvent',
    'MessageReactionAddData',
    'MessageReactionAddEvent',
    'MessageReactionRemoveData',
    'MessageReactionRemoveEvent',
    'MessageReactionRemoveAllData',
    'MessageReactionRemoveAllEvent',
    'MessageReactionRemoveEmojiData',
    'MessageReactionRemoveEmojiEvent',
    'PresenceUpdateData',
    'ClientStatusData',
    'PartialActivityData',
    'ActivityData',
    'ActivityTypes',
    'ActivityTimestampsData',
    'ActivityEmojiData',
    'ActivityPartyData',
    'ActivityAssetsData',
    'ActivitySecretsData',
    'ActivityButtonData',
    'TypingStartData',
    'TypingStartEvent',
    'UserUpdateData',
    'UserUpdateEvent',
    'VoiceStateUpdateData',
    'VoiceStateUpdateEvent',
    'VoiceServerUpdateData',
    'VoiceServerUpdateEvent',
    'WebhooksUpdateData',
    'WebhooksUpdateEvent',
    'InteractionCreateData',
    'InteractionCreateEvent',
    'StageInstanceCreateData',
    'StageInstanceCreateEvent',
    'StageInstanceUpdateData',
    'StageInstanceUpdateEvent',
    'StageInstanceDeleteData',
    'StageInstanceDeleteEvent',
    'DispatchEvent',
    'GatewayCommand',
    'GatewayEvent',
)


_D = TypeVar('_D', bound='Mapping[str, Any]')
_T = TypeVar('_T', bound='str')  # Literal


# https://discord.com/developers/docs/topics/gateway-events#get-gateway-example-response


class GetGatewayData(TypedDict):
    url: str


# https://discord.com/developers/docs/topics/gateway#get-gateway-bot


class GetGatewayBotData(TypedDict):
    url: str
    shards: int
    session_start_limit: 'discord_typings.SessionStartLimitData'


# https://discord.com/developers/docs/topics/gateway#session-start-limit-object


class SessionStartLimitData(TypedDict):
    total: int
    remaining: int
    reset_after: int
    max_concurrency: int


# https://discord.com/developers/docs/topics/gateway-events#payload-structure


class GenericDispatchEvent(TypedDict, Generic[_T, _D]):
    """Generic Discord dispatch event.

    This is a generic TypedDict for creating typings for dispatch events. The
    resulting TypedDict contains the `op`, `d`, `s` and `t` fields. To get the
    typing for the inner `d` key, grab the second argument to the generic.

    The reason this doesn't have a leading underscore is to look nicer when
    previewed in editors and IDEs but the actual `GenericDispatchEvent()`
    should be considered private - use the public, typed, versions.
    """
    op: Literal[0]
    d: _D
    s: int
    t: _T


# https://discord.com/developers/docs/topics/gateway-events#identify


class IdentifyData(TypedDict):
    token: str
    properties: 'discord_typings.IdentifyConnectionPropertiesData'
    compress: NotRequired[bool]
    large_threshold: NotRequired[int]
    shard: NotRequired[Union[Tuple[int, int], List[int]]]
    presence: NotRequired['discord_typings.UpdatePresenceData']
    intents: int


class IdentifyConnectionPropertiesData(TypedDict):
    os: str
    browser: str
    device: str


class IdentifyCommand(TypedDict):
    op: Literal[2]
    d: IdentifyData


# https://discord.com/developers/docs/topics/gateway-events#resume


class ResumeData(TypedDict):
    token: str
    session_id: str
    seq: int


class ResumeCommand(TypedDict):
    op: Literal[6]
    d: ResumeData


# https://discord.com/developers/docs/topics/gateway-events#heartbeat


class HeartbeatCommand(TypedDict):
    op: Literal[1]
    d: Optional[int]


# https://discord.com/developers/docs/topics/gateway-events#request-guild-members


class _QueryRequestMembersCommand(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    query: str
    limit: int
    presences: NotRequired[bool]
    user_ids: NotRequired[Union[
        'discord_typings.Snowflake',
        List['discord_typings.Snowflake'],
    ]]
    nonce: NotRequired[str]


class _UserIDsRequestMembersCommand(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    presences: NotRequired[bool]
    user_ids: Union['discord_typings.Snowflake', List['discord_typings.Snowflake']]
    nonce: NotRequired[str]


# This enforces the fact that 'limit' is required when 'query' is set.
RequestGuildMembersData = Union[_QueryRequestMembersCommand, _UserIDsRequestMembersCommand]


class RequestGuildMembersCommand(TypedDict):
    op: Literal[8]
    d: RequestGuildMembersData


# https://discord.com/developers/docs/topics/gateway-events#update-voice-state


class UpdateVoiceStateData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    channel_id: Optional['discord_typings.Snowflake']
    self_mute: bool
    self_deaf: bool


class UpdateVoiceStateCommand(TypedDict):
    op: Literal[4]
    d: UpdateVoiceStateData


# https://discord.com/developers/docs/topics/gateway-events#update-presence


class UpdatePresenceData(TypedDict):
    since: Optional[int]
    activities: List['discord_typings.PartialActivityData']
    status: Literal['online', 'idle', 'dnd', 'invisible']
    afk: bool


class UpdatePresenceCommand(TypedDict):
    op: Literal[3]
    d: UpdatePresenceData


# https://discord.com/developers/docs/topics/gateway-events#hello


class HelloData(TypedDict):
    heartbeat_interval: int


class HelloEvent(TypedDict):
    op: Literal[10]
    d: HelloData
    s: None
    t: None


# https://discord.com/developers/docs/topics/gateway#heartbeat-interval


class HeartbeatACKEvent(TypedDict):
    op: Literal[11]


# https://discord.com/developers/docs/topics/gateway-events#ready


class PartialApplicationData(TypedDict):
    id: 'discord_typings.Snowflake'
    flags: int


class ReadyData(TypedDict):
    v: int
    user: 'discord_typings.UserData'
    guilds: List['discord_typings.UnavailableGuildData']
    session_id: str
    resume_gateway_url: str
    shard: NotRequired[Union[Tuple[int, int], List[int]]]
    application: PartialApplicationData


ReadyEvent = GenericDispatchEvent[Literal['READY'], ReadyData]


# https://discord.com/developers/docs/topics/gateway-events#resumed


class ResumedData(TypedDict):
    ...  # It only has an undocumented _trace field


ResumedEvent = GenericDispatchEvent[Literal['RESUMED'], ResumedData]


# https://discord.com/developers/docs/topics/gateway-events#reconnect


class ReconnectEvent(TypedDict):
    op: Literal[7]
    d: None
    s: None
    t: None


# https://discord.com/developers/docs/topics/gateway-events#invalid-session


class InvalidSessionEvent(TypedDict):
    op: Literal[9]
    d: bool
    s: None
    t: None


# https://discord.com/developers/docs/topics/gateway-events#application-command-permissions-update


# Line too long
ApplicationCommandPermissionsUpdateData: TypeAlias = (
    'discord_typings.ApplicationCommandPermissionsData'
)


ApplicationCommandPermissionsUpdateEvent = GenericDispatchEvent[
    Literal['APPLICATION_COMMAND_PERMISSIONS_UPDATE'],
    ApplicationCommandPermissionsUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#auto-moderation-rule-create


AutoModerationRuleCreateData: TypeAlias = 'discord_typings.AutoModerationRuleData'


AutoModerationRuleCreateEvent = GenericDispatchEvent[
    Literal['AUTO_MODERATION_RULE_CREATE'],
    AutoModerationRuleCreateData
]


# https://discord.com/developers/docs/topics/gateway-events#auto-moderation-rule-update


AutoModerationRuleUpdateData: TypeAlias = 'discord_typings.AutoModerationRuleData'


AutoModerationRuleUpdateEvent = GenericDispatchEvent[
    Literal['AUTO_MODERATION_RULE_UPDATE'],
    AutoModerationRuleUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#auto-moderation-rule-delete


AutoModerationRuleDeleteData: TypeAlias = 'discord_typings.AutoModerationRuleData'


AutoModerationRuleDeleteEvent = GenericDispatchEvent[
    Literal['AUTO_MODERATION_RULE_DELETE'],
    AutoModerationRuleDeleteData
]


# https://discord.com/developers/docs/topics/gateway-events#auto-moderation-action-execution


class AutoModerationActionExecutionData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    action: 'discord_typings.AutoModerationActionData'
    rule_id: 'discord_typings.Snowflake'
    rule_trigger_type: 'discord_typings.AutoModerationTriggerTypes'
    user_id: 'discord_typings.Snowflake'
    channel_id: NotRequired['discord_typings.Snowflake']
    message_id: NotRequired['discord_typings.Snowflake']
    alert_system_message_id: NotRequired['discord_typings.Snowflake']
    content: NotRequired[str]
    matched_keyword: Optional[str]
    matched_content: NotRequired[Optional[str]]


AutoModerationActionExecutionEvent = GenericDispatchEvent[
    Literal['AUTO_MODERATION_ACTION_EXECUTION'],
    AutoModerationActionExecutionData
]


# https://discord.com/developers/docs/topics/gateway-events#channels


# Utility for the events below
_GuildChannelData = Union[
    'discord_typings.TextChannelData',
    'discord_typings.NewsChannelData',
    'discord_typings.VoiceChannelData',
    'discord_typings.CategoryChannelData',
    'discord_typings.ForumChannelData',
    'discord_typings.MediaChannelData',
]


# https://discord.com/developers/docs/topics/gateway-events#channel-create


ChannelCreateData = _GuildChannelData
ChannelCreateEvent = GenericDispatchEvent[Literal['CHANNEL_CREATE'], ChannelCreateData]


# https://discord.com/developers/docs/topics/gateway-events#channel-update


ChannelUpdateData = _GuildChannelData
ChannelUpdateEvent = GenericDispatchEvent[Literal['CHANNEL_UPDATE'], ChannelUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#channel-delete


ChannelDeleteData = _GuildChannelData
ChannelDeleteEvent = GenericDispatchEvent[Literal['CHANNEl_DELETE'], ChannelDeleteData]


# https://discord.com/developers/docs/topics/gateway-events#thread-create


class ThreadCreateData(discord_typings.ThreadChannelData):
    newly_created: bool  # Extra THREAD_CREATE field


ThreadCreateEvent = GenericDispatchEvent[Literal['THREAD_CREATE'], ThreadCreateData]


# https://discord.com/developers/docs/topics/gateway-events#thread-update


ThreadUpdateData: TypeAlias = 'discord_typings.ThreadChannelData'
ThreadUpdateEvent = GenericDispatchEvent[Literal['THREAD_UPDATE'], ThreadUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#thread-delete


class ThreadDeleteData(TypedDict):
    id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'
    parent_id: 'discord_typings.Snowflake'
    type: Literal[10, 11, 12]


ThreadDeleteEvent = GenericDispatchEvent[Literal['THREAD_DELETE'], ThreadDeleteData]


# https://discord.com/developers/docs/topics/gateway-events#thread-list-sync


class ThreadListSyncData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    channel_ids: NotRequired[List['discord_typings.Snowflake']]
    threads: List['discord_typings.ThreadChannelData']
    members: List['discord_typings.ThreadMemberData']


ThreadListSyncEvent = GenericDispatchEvent[Literal['THREAD_LIST_SYNC'], ThreadListSyncData]


# https://discord.com/developers/docs/topics/gateway-events#thread-member-update


class ThreadMemberUpdateData(TypedDict):
    # 'id' and 'user_id' is only missing in the GUILD_CREATE event, so we know
    # that they are present in this event (hence the missing NotRequired
    # compared to ThreadMemberData).
    id: 'discord_typings.Snowflake'
    user_id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'
    member: NotRequired['discord_typings.GuildMemberData']
    join_timestamp: str
    flags: int


ThreadMemberUpdateEvent = GenericDispatchEvent[
    Literal['THREAD_MEMBER_UPDATE'], ThreadMemberUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#thread-members-update


class ThreadMembersUpdateData(TypedDict):
    id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'
    member_count: int
    added_members: NotRequired[List['discord_typings.ThreadMemberData']]
    removed_member_ids: NotRequired[List['discord_typings.Snowflake']]


ThreadMembersUpdateEvent = GenericDispatchEvent[
    Literal['THREAD_MEMBERS_UPDATE'], ThreadMembersUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#channel-pins-update


class ChannelPinsUpdateData(TypedDict):
    guild_id: NotRequired['discord_typings.Snowflake']
    channel_id: 'discord_typings.Snowflake'
    last_pin_timestamp: NotRequired[Optional[str]]


ChannelPinsUpdateEvent = GenericDispatchEvent[
    Literal['CHANNEL_PINS_UPDATE'], ChannelPinsUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-create


class GuildCreateData(discord_typings.GuildData):
    # Extra GUILD_CREATE fields
    joined_at: str
    large: bool
    unavailable: bool
    member_count: int
    voice_states: List['discord_typings.VoiceStateData']
    members: List['discord_typings.GuildMemberData']
    channels: List[_GuildChannelData]  # Alias from above
    threads: List['discord_typings.ThreadChannelData']
    presences: List['discord_typings.UpdatePresenceData']
    stage_instances: List['discord_typings.StageInstanceData']
    guild_scheduled_events: List['discord_typings.GuildScheduledEventData']


GuildCreateEvent = GenericDispatchEvent[Literal['GUILD_CREATE'], GuildCreateData]


# https://discord.com/developers/docs/topics/gateway-events#guild-update


GuildUpdateData: TypeAlias = 'discord_typings.GuildData'
GuildUpdateEvent = GenericDispatchEvent[Literal['GUILD_UPDATE'], GuildUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#guild-delete


GuildDeleteData: TypeAlias = 'discord_typings.UnavailableGuildData'
GuildDeleteEvent = GenericDispatchEvent[Literal['GUILD_DELETE'], 'GuildDeleteData']


# https://discord.com/developers/docs/topics/gateway-events#guild-audit-log-entry-create


GuildAuditLogEntryCreateData: TypeAlias = 'discord_typings.AuditLogEntryData'
GuildAuditLogEntryCreateEvent = GenericDispatchEvent[
    Literal['GUILD_AUDIT_LOG_ENTRY_CREATE'],
    GuildAuditLogEntryCreateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-ban-add


class GuildBanAddData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    user: 'discord_typings.UserData'


GuildBanAddEvent = GenericDispatchEvent[Literal['GUILD_BAN_ADD'], GuildBanAddData]


# https://discord.com/developers/docs/topics/gateway-events#guild-ban-remove


class GuildBanRemoveData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    user: 'discord_typings.UserData'


GuildBanRemoveEvent = GenericDispatchEvent[Literal['GUILD_BAN_REMOVE'], GuildBanRemoveData]


# https://discord.com/developers/docs/topics/gateway-events#guild-emojis-update


class GuildEmojisUpdateData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    emojis: List['discord_typings.EmojiData']


GuildEmojisUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_EMOJIS_UPDATE'], GuildEmojisUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-stickers-update


class GuildStickersUpdateData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    stickers: List['discord_typings.StickerData']


GuildStickersUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_STICKERS_UPDATE'], GuildStickersUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-integrations-update


class GuildIntergrationsUpdateData(TypedDict):
    guild_id: 'discord_typings.Snowflake'


GuildIntergrationsUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_INTEGRATIONS_UPDATE'], GuildIntergrationsUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-member-add


class GuildMemberAddData(TypedDict):
    user: 'discord_typings.UserData'  # Always present in GUILD_MEMBER_ADD events
    nick: NotRequired[Optional[str]]
    avatar: NotRequired[Optional[str]]
    roles: List['discord_typings.Snowflake']
    joined_at: str
    premium_since: NotRequired[Optional[str]]
    deaf: bool
    mute: bool
    pending: NotRequired[bool]
    permissions: NotRequired[str]
    communication_disabled_until: NotRequired[Optional[str]]

    guild_id: 'discord_typings.Snowflake'  # Extra field


GuildMemberAddEvent = GenericDispatchEvent[
    Literal['GUILD_MEMBER_ADD'], GuildMemberAddData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-member-remove


class GuildMemberRemoveData(TypedDict):
    user: 'discord_typings.UserData'
    guild_id: 'discord_typings.Snowflake'


GuildMemberRemoveEvent = GenericDispatchEvent[
    Literal['GUILD_MEMBER_REMOVE'], GuildMemberRemoveData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-member-update


class GuildMemberUpdateData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    roles: List['discord_typings.Snowflake']
    user: 'discord_typings.UserData'
    nick: NotRequired[Optional[str]]
    avatar: Optional[str]
    joined_at: Optional[str]
    premium_since: NotRequired[Optional[str]]
    deaf: NotRequired[bool]
    mute: NotRequired[bool]
    pending: NotRequired[bool]
    communication_disabled_until: NotRequired[Optional[str]]


GuildMemberUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_MEMBER_UPDATE'], GuildMemberUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-members-chunk


class GuildMembersChunkData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    members: List['discord_typings.GuildMemberData']
    chunk_index: int
    chunk_count: int
    not_found: NotRequired[List['discord_typings.Snowflake']]
    presences: NotRequired[List['discord_typings.PresenceUpdateData']]
    nonce: NotRequired[str]


GuildMembersChunkEvent = GenericDispatchEvent[
    Literal['GUILD_MEMBERS_CHUNK'], GuildMembersChunkData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-role-create


class GuildRoleCreateData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    role: 'discord_typings.RoleData'


GuildRoleCreateEvent = GenericDispatchEvent[Literal['GUILD_ROLE_CREATE'], GuildRoleCreateData]


# https://discord.com/developers/docs/topics/gateway-events#guild-role-update


class GuildRoleUpdateData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    role: 'discord_typings.RoleData'


GuildRoleUpdateEvent = GenericDispatchEvent[Literal['GUILD_ROLE_UPDATE'], GuildRoleUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#guild-role-delete


class GuildRoleDeleteData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    role_id: 'discord_typings.Snowflake'


GuildRoleDeleteEvent = GenericDispatchEvent[Literal['GUILD_ROLE_DELETE'], GuildRoleDeleteData]


# https://discord.com/developers/docs/topics/gateway-events#guild-scheduled-event-create


GuildScheduledEventCreateData: TypeAlias = 'discord_typings.GuildScheduledEventData'
GuildScheduledEventCreateEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_CREATE'], GuildScheduledEventCreateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-scheduled-event-update


GuildScheduledEventUpdateData: TypeAlias = 'discord_typings.GuildScheduledEventData'
GuildScheduledEventUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_UPDATE'], GuildScheduledEventUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-scheduled-event-delete


GuildScheduledEventDeleteData: TypeAlias = 'discord_typings.GuildScheduledEventData'
GuildScheduledEventDeleteEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_DELETE'], GuildScheduledEventDeleteData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-scheduled-event-user-add


class GuildScheduledEventUserAddData(TypedDict):
    guild_scheduled_event_id: 'discord_typings.Snowflake'
    user_id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'


GuildScheduledEventUserAddEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_USER_ADD'], GuildScheduledEventUserAddData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-scheduled-event-user-remove


class GuildScheduledEventUserRemoveData(TypedDict):
    guild_scheduled_event_id: 'discord_typings.Snowflake'
    user_id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'


GuildScheduledEventUserRemoveEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_USER_REMOVE'], GuildScheduledEventUserRemoveData
]


# https://discord.com/developers/docs/topics/gateway-events#integrations


class _StreamingIntegrationGuildData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    type: Literal['twitch', 'youtube', 'discord']
    enabled: bool
    syncing: bool
    role_id: NotRequired['discord_typings.Snowflake']
    enable_emoticons: bool
    expire_behavior: 'discord_typings.IntegrationExpireBehaviors'
    expire_grace_period: int
    user: NotRequired['discord_typings.UserData']
    account: 'discord_typings.IntegrationAccountData'
    synced_at: str
    subscriber_count: int
    revoked: bool
    application: 'discord_typings.IntegrationApplicationData'
    scopes: NotRequired[List['discord_typings.OAuth2Scopes']]

    guild_id: 'discord_typings.Snowflake'


class _DiscordIntegrationGuildData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    type: Literal['discord']
    enabled: bool
    user: NotRequired['discord_typings.UserData']
    account: 'discord_typings.IntegrationAccountData'
    application: NotRequired['discord_typings.IntegrationApplicationData']
    scopes: NotRequired[List['discord_typings.OAuth2Scopes']]

    guild_id: 'discord_typings.Snowflake'


# Integration object, with an additional guild_id field
_IntegrationGuildData = Union[_StreamingIntegrationGuildData, _DiscordIntegrationGuildData]

# https://discord.com/developers/docs/topics/gateway-events#integration-create


IntegrationCreateData: TypeAlias = '_IntegrationGuildData'
IntegrationCreateEvent = GenericDispatchEvent[
    Literal['INTEGRATION_CREATE'], IntegrationCreateData
]


# https://discord.com/developers/docs/topics/gateway-events#integration-update


IntegrationUpdateData: TypeAlias = '_IntegrationGuildData'
IntegrationUpdateEvent = GenericDispatchEvent[
    Literal['INTEGRATION_UPDATE'], IntegrationUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#integration-delete


class IntegrationDeleteData(TypedDict):
    id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'
    application_id: NotRequired['discord_typings.Snowflake']


IntegrationDeleteEvent = GenericDispatchEvent[
    Literal['INTEGRATION_DELETE'], IntegrationDeleteData
]


# https://discord.com/developers/docs/topics/gateway-events#invite-create


class InviteCreateData(TypedDict):
    channel_id: 'discord_typings.Snowflake'
    code: str
    created_at: str
    guild_id: NotRequired['discord_typings.Snowflake']
    inviter: NotRequired['discord_typings.UserData']
    max_age: int
    max_uses: int
    target_type: NotRequired[Literal[1, 2]]
    target_user: NotRequired['discord_typings.UserData']
    target_application: NotRequired['discord_typings.ApplicationData']
    temporary: bool
    uses: int


InviteCreateEvent = GenericDispatchEvent[Literal['INVITE_CREATE'], InviteCreateData]


# https://discord.com/developers/docs/topics/gateway-events#invite-delete


class InviteDeleteData(TypedDict):
    channel_id: 'discord_typings.Snowflake'
    guild_id: NotRequired['discord_typings.Snowflake']
    code: str


InviteDeleteEvent = GenericDispatchEvent[Literal['INVITE_DELETE'], InviteDeleteData]


# https://discord.com/developers/docs/topics/gateway-events#message-create


MessageCreateData: TypeAlias = 'discord_typings.MessageData'
MessageCreateEvent = GenericDispatchEvent[Literal['MESSAGE_CREATE'], MessageCreateData]


# https://discord.com/developers/docs/topics/gateway-events#message-update


MessageUpdateData: TypeAlias = 'discord_typings.MessageData'
MessageUpdateEvent = GenericDispatchEvent[Literal['MESSAGE_UPDATE'], MessageUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#message-delete


class MessageDeleteData(TypedDict):
    id: 'discord_typings.Snowflake'
    channel_id: 'discord_typings.Snowflake'
    guild_id: NotRequired['discord_typings.Snowflake']


MessageDeleteEvent = GenericDispatchEvent[Literal['MESSAGE_DELETE'], MessageDeleteData]


# https://discord.com/developers/docs/topics/gateway-events#message-delete-bulk


class MessageDeleteBulkData(TypedDict):
    ids: List['discord_typings.Snowflake']
    channel_id: 'discord_typings.Snowflake'
    guild_id: NotRequired['discord_typings.Snowflake']


MessageDeleteBulkEvent = GenericDispatchEvent[
    Literal['MESSAGE_DELETE_BULK'], MessageDeleteBulkData
]


# https://discord.com/developers/docs/topics/gateway-events#message-reaction-add


class MessageReactionAddData(TypedDict):
    user_id: 'discord_typings.Snowflake'
    channel_id: 'discord_typings.Snowflake'
    message_id: 'discord_typings.Snowflake'
    guild_id: NotRequired['discord_typings.Snowflake']
    member: NotRequired['discord_typings.GuildMemberData']
    emoji: 'discord_typings.EmojiData'
    message_author_id: NotRequired['discord_typings.Snowflake']


MessageReactionAddEvent = GenericDispatchEvent[
    Literal['MESSAGE_REACTION_ADD'], MessageReactionAddData
]


# https://discord.com/developers/docs/topics/gateway-events#message-reaction-remove


class MessageReactionRemoveData(TypedDict):
    user_id: 'discord_typings.Snowflake'
    channel_id: 'discord_typings.Snowflake'
    message_id: 'discord_typings.Snowflake'
    guild_id: NotRequired['discord_typings.Snowflake']
    emoji: 'discord_typings.EmojiData'


MessageReactionRemoveEvent = GenericDispatchEvent[
    Literal['MESSAGE_REACTION_REMOVE'], MessageReactionRemoveData
]


# https://discord.com/developers/docs/topics/gateway-events#message-reaction-remove-all


class MessageReactionRemoveAllData(TypedDict):
    channel_id: 'discord_typings.Snowflake'
    message_id: 'discord_typings.Snowflake'
    guild_id: NotRequired['discord_typings.Snowflake']


MessageReactionRemoveAllEvent = GenericDispatchEvent[
    Literal['MESSAGE_REACTION_REMOVE_ALL'], MessageReactionRemoveAllData
]


# https://discord.com/developers/docs/topics/gateway-events#message-reaction-remove-emoji


class MessageReactionRemoveEmojiData(TypedDict):
    channel_id: 'discord_typings.Snowflake'
    guild_id: NotRequired['discord_typings.Snowflake']
    message_id: 'discord_typings.Snowflake'
    emoji: 'discord_typings.EmojiData'


MessageReactionRemoveEmojiEvent = GenericDispatchEvent[
    Literal['MESSAGE_REACTION_REMOVE_EMOJI'], MessageReactionRemoveEmojiData
]


# https://discord.com/developers/docs/topics/gateway-events#presence-update


class PresenceUpdateData(TypedDict):
    user: 'discord_typings.UserData'
    guild_id: 'discord_typings.Snowflake'
    status: Literal['idle', 'dnd', 'online', 'offline']
    activities: List['discord_typings.ActivityData']
    client_status: 'discord_typings.ClientStatusData'


class ClientStatusData(TypedDict):
    desktop: NotRequired[str]
    mobile: NotRequired[str]
    web: NotRequired[str]


# https://discord.com/developers/docs/topics/gateway-events#activity-object


class PartialActivityData(TypedDict):
    name: str
    type: 'discord_typings.ActivityTypes'
    state: NotRequired[Optional[str]]
    url: NotRequired[str]


class ActivityData(TypedDict):
    name: str
    type: Literal[0, 1, 2, 3, 4, 5]
    url: NotRequired[Optional[str]]
    created_at: int
    timestamps: NotRequired['discord_typings.ActivityTimestampsData']
    application_id: NotRequired['discord_typings.Snowflake']
    details: NotRequired[Optional[str]]
    state: NotRequired[Optional[str]]
    emoji: NotRequired[Optional['discord_typings.ActivityEmojiData']]
    party: NotRequired[Optional['discord_typings.ActivityPartyData']]
    assets: NotRequired['discord_typings.ActivityAssetsData']
    secrets: NotRequired['discord_typings.ActivitySecretsData']
    instance: NotRequired[bool]
    flags: NotRequired[int]
    buttons: NotRequired[List['discord_typings.ActivityButtonData']]


# https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-types


ActivityTypes = Literal[0, 1, 2, 3, 4, 5]


# https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-timestamps


class ActivityTimestampsData(TypedDict):
    start: NotRequired[int]
    end: NotRequired[int]


# https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-emoji


class ActivityEmojiData(TypedDict):
    name: str
    id: NotRequired['discord_typings.Snowflake']
    animated: NotRequired[bool]


# https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-party


class ActivityPartyData(TypedDict):
    id: NotRequired[str]
    size: NotRequired[Union[Tuple[int, int], List[int]]]


# https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-assets


class ActivityAssetsData(TypedDict):
    large_image: NotRequired[str]
    large_text: NotRequired[str]
    small_image: NotRequired[str]
    small_test: NotRequired[str]


# https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-secrets


class ActivitySecretsData(TypedDict):
    join: NotRequired[str]
    spectate: NotRequired[str]
    match: NotRequired[str]


# https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-buttons


class ActivityButtonData(TypedDict):
    label: str
    url: str


# https://discord.com/developers/docs/topics/gateway-events#typing-start


class TypingStartData(TypedDict):
    channel_id: 'discord_typings.Snowflake'
    guild_id: NotRequired['discord_typings.Snowflake']
    user_id: 'discord_typings.Snowflake'
    timestamp: int
    member: NotRequired['discord_typings.GuildMemberData']


TypingStartEvent = GenericDispatchEvent[Literal['TYPING_START'], TypingStartData]


# https://discord.com/developers/docs/topics/gateway-events#user-update


UserUpdateData: TypeAlias = 'discord_typings.UserData'
UserUpdateEvent = GenericDispatchEvent[Literal['USER_UPDATE'], UserUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#voice-state-update


VoiceStateUpdateData: TypeAlias = 'discord_typings.VoiceStateData'
VoiceStateUpdateEvent = GenericDispatchEvent[
    Literal['VOICE_STATUS_UPDATE'], VoiceStateUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#voice-server-update


class VoiceServerUpdateData(TypedDict):
    token: str
    guild_id: 'discord_typings.Snowflake'
    endpoint: Optional[str]


VoiceServerUpdateEvent = GenericDispatchEvent[
    Literal['VOICE_SERVER_UPDATE'], VoiceServerUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#webhooks-update


class WebhooksUpdateData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    channel_id: 'discord_typings.Snowflake'


WebhooksUpdateEvent = GenericDispatchEvent[Literal['WEBHOOKS_UPDATE'], WebhooksUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#interaction-create


InteractionCreateData: TypeAlias = 'discord_typings.InteractionData'
InteractionCreateEvent = GenericDispatchEvent[
    Literal['INTERACTION_CREATE'], InteractionCreateData
]


# https://discord.com/developers/docs/topics/gateway-events#stage-instance-create


StageInstanceCreateData: TypeAlias = 'discord_typings.StageInstanceData'
StageInstanceCreateEvent = GenericDispatchEvent[
    Literal['STAGE_INSTANCE_CREATE'], StageInstanceCreateData
]


# https://discord.com/developers/docs/topics/gateway-events#stage-instance-update


StageInstanceUpdateData: TypeAlias = 'discord_typings.StageInstanceData'
StageInstanceUpdateEvent = GenericDispatchEvent[
    Literal['STAGE_INSTANCE_UPDATE'], StageInstanceUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#stage-instance-delete


StageInstanceDeleteData: TypeAlias = 'discord_typings.StageInstanceData'
StageInstanceDeleteEvent = GenericDispatchEvent[
    Literal['STAGE_INSTANCE_DELETE'], StageInstanceDeleteData
]


# Generalized unions for the typings in this file


DispatchEvent = GenericDispatchEvent[str, Dict[str, Any]]


GatewayCommand = Union[
    IdentifyCommand,
    ResumeCommand,
    HeartbeatCommand,
    RequestGuildMembersCommand,
    UpdateVoiceStateCommand,
    UpdatePresenceCommand,
]


GatewayEvent = Union[
    HelloEvent,
    HeartbeatACKEvent,
    ReadyEvent,
    ResumedEvent,
    ReconnectEvent,
    InvalidSessionEvent,
    DispatchEvent,
]
