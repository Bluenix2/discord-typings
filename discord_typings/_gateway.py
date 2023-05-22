from __future__ import annotations

from typing import (
    TYPE_CHECKING, Any, Dict, Generic, List, Mapping, Optional, Tuple, TypeVar,
    Union
)

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict, final

if TYPE_CHECKING:
    # Flake8 complains about some of these imports where they are only used
    # inside of strings (not annotations) for the type aliases, so we have to
    # disable the check.
    from ._interactions import (  # noqa: F401
        ApplicationCommandPermissionsData, InteractionData
    )
    from ._reference import Locales, Snowflake
    from ._resources import (  # noqa: F401
        ApplicationData, AuditLogEntryData, AutoModerationActionData,
        AutoModerationRuleData, AutoModerationTriggerTypes,
        CategoryChannelData, EmojiData, GuildData, GuildFeaturesData,
        GuildMemberData, GuildScheduledEventData, IntegrationAccountData,
        IntegrationApplicationData, IntegrationExpireBehaviors, MessageData,
        NewsChannelData, RoleData, StageInstanceData, StickerData,
        TextChannelData, ThreadChannelData, ThreadMemberData,
        ThreadMetadataData, UnavailableGuildData, UserData, VoiceChannelData,
        VoiceStateData, WelcomeScreenData
    )

__all__ = (
    'HeartbeatACKEvent', 'IdentifyData', 'IdentifyConnectionProperties', 'IdentifyCommand',
    'ResumeData', 'ResumeCommand', 'HeartbeatCommand', 'RequestGuildMembersData',
    'RequestGuildMembersCommand', 'UpdateVoiceStateData', 'UpdateVoiceStateCommand',
    'PartialActivityData', 'UpdatePresenceData', 'UpdatePresenceCommand', 'HelloData',
    'HelloEvent', 'PartialApplicationData', 'ReadyData', 'ReadyEvent', 'ResumedData',
    'ResumedEvent', 'ReconnectEvent', 'InvalidSessionEvent',
    'ApplicationCommandPermissionsUpdateData', 'ApplicationCommandPermissionsUpdateEvent',
    'ChannelCreateData', 'ChannelCreateEvent', 'ChannelUpdateData', 'ChannelUpdateEvent',
    'ChannelDeleteData', 'ChannelDeleteEvent', 'ThreadCreateData', 'ThreadCreateEvent',
    'ThreadUpdateData', 'ThreadUpdateEvent', 'ThreadDeleteData', 'ThreadDeleteEvent',
    'ThreadListSyncData', 'ThreadListSyncEvent', 'ThreadMemberUpdateData',
    'ThreadMemberUpdateEvent', 'ThreadMembersUpdateData', 'ThreadMembersUpdateEvent',
    'ChannelPinsUpdateData', 'ChannelPinsUpdateEvent', 'GuildCreateData', 'GuildCreateEvent',
    'GuildUpdateData', 'GuildUpdateEvent', 'GuildDeleteData', 'GuildDeleteEvent',
    'GuildBanAddData', 'GuildBanAddEvent', 'GuildBanRemoveData', 'GuildBanRemoveEvent',
    'GuildEmojisUpdateData', 'GuildEmojisUpdateEvent', 'GuildStickersUpdateData',
    'GuildStickersUpdateEvent', 'GuildIntergrationsUpdateData',
    'GuildIntergrationsUpdateEvent', 'GuildMemberAddData', 'GuildMemberAddEvent',
    'GuildMemberRemoveData', 'GuildMemberRemoveEvent', 'GuildMemberUpdateData',
    'GuildMemberUpdateEvent', 'GuildMembersChunkData', 'GuildMembersChunkEvent',
    'GuildRoleCreateData', 'GuildRoleCreateEvent', 'GuildRoleCreateEvent',
    'GuildRoleUpdateData', 'GuildRoleUpdateEvent', 'GuildRoleDeleteData',
    'GuildRoleDeleteEvent', 'GuildScheduledEventCreateData', 'GuildScheduledEventCreateEvent',
    'GuildScheduledEventUpdateData', 'GuildScheduledEventUpdateEvent',
    'GuildScheduledEventDeleteData', 'GuildScheduledEventDeleteEvent',
    'GuildScheduledEventUserAddData', 'GuildScheduledEventUserAddEvent',
    'GuildScheduledEventUserRemoveData', 'GuildScheduledEventUserRemoveEvent',
    'IntegrationCreateData', 'IntegrationCreateEvent', 'IntegrationUpdateData',
    'IntegrationUpdateEvent', 'IntegrationDeleteData', 'IntegrationDeleteEvent',
    'InviteCreateData', 'InviteCreateEvent', 'InviteDeleteData', 'InviteDeleteEvent',
    'MessageCreateData', 'MessageCreateEvent', 'MessageUpdateData', 'MessageUpdateEvent',
    'MessageDeleteData', 'MessageDeleteEvent', 'MessageDeleteBulkData',
    'MessageDeleteBulkEvent', 'MessageReactionAddData', 'MessageReactionAddEvent',
    'MessageReactionRemoveData', 'MessageReactionRemoveEvent', 'MessageReactionRemoveAllData',
    'MessageReactionRemoveAllEvent', 'MessageReactionRemoveEmojiData',
    'MessageReactionRemoveEmojiEvent', 'PresenceUpdateData', 'ClientStatusData',
    'ActivityData', 'ActivityTimestampsData', 'ActivityEmojiData', 'ActivityPartyData',
    'ActivityAssetsData', 'ActivitySecretsData', 'ActivityButtonData', 'TypingStartData',
    'TypingStartEvent', 'UserUpdateData', 'UserUpdateEvent', 'VoiceStateUpdateData',
    'VoiceStateUpdateEvent', 'VoiceServerUpdateData', 'VoiceServerUpdateEvent',
    'WebhooksUpdateData', 'WebhooksUpdateEvent', 'InteractionCreateData',
    'InteractionCreateEvent', 'StageInstanceCreateData', 'StageInstanceCreateEvent',
    'StageInstanceUpdateData', 'StageInstanceUpdateEvent', 'StageInstanceDeleteData',
    'StageInstanceDeleteEvent', 'GetGatewayData', 'GetGatewayBotData',
    'SessionStartLimitData', 'DispatchEvent', 'GatewayEvent',
    'GuildAuditLogEntryCreateData', 'GuildAuditLogEntryCreateEvent'
)


_D = TypeVar('_D', bound='Mapping[str, Any]')
_T = TypeVar('_T', bound='str')  # Literal


@final
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


# https://discord.com/developers/docs/topics/gateway#heartbeat-interval


@final
class HeartbeatACKEvent(TypedDict):
    op: Literal[11]


# https://discord.com/developers/docs/topics/gateway-events#identify


@final
class IdentifyData(TypedDict):
    token: str
    properties: IdentifyConnectionProperties
    compress: NotRequired[bool]
    large_threshold: NotRequired[int]
    shard: NotRequired[Union[Tuple[int, int], List[int]]]
    presence: NotRequired[UpdatePresenceData]
    intents: int


@final
class IdentifyConnectionProperties(TypedDict):
    os: str
    browser: str
    device: str


@final
class IdentifyCommand(TypedDict):
    op: Literal[2]
    d: IdentifyData

# https://discord.com/developers/docs/topics/gateway-events#resume


@final
class ResumeData(TypedDict):
    token: str
    session_id: str
    seq: int


@final
class ResumeCommand(TypedDict):
    op: Literal[6]
    d: ResumeData


# https://discord.com/developers/docs/topics/gateway-events#heartbeat


@final
class HeartbeatCommand(TypedDict):
    op: Literal[1]
    d: Optional[int]


# https://discord.com/developers/docs/topics/gateway-events#request-guild-members


@final
class _QueryRequestMembersCommand(TypedDict):
    guild_id: Snowflake
    query: str
    limit: int
    presences: NotRequired[bool]
    user_ids: NotRequired[Union[Snowflake, List[Snowflake]]]
    nonce: NotRequired[str]


@final
class _UserIDsRequestMembersCommand(TypedDict):
    guild_id: Snowflake
    presences: NotRequired[bool]
    user_ids: Union[Snowflake, List[Snowflake]]
    nonce: NotRequired[str]


# This enforces the fact that 'limit' is required when 'query' is set.
RequestGuildMembersData = Union[_QueryRequestMembersCommand, _UserIDsRequestMembersCommand]


@final
class RequestGuildMembersCommand(TypedDict):
    op: Literal[8]
    d: RequestGuildMembersData


# https://discord.com/developers/docs/topics/gateway-events#update-voice-state


@final
class UpdateVoiceStateData(TypedDict):
    guild_id: Snowflake
    channel_id: Optional[Snowflake]
    self_mute: bool
    self_deaf: bool


@final
class UpdateVoiceStateCommand(TypedDict):
    op: Literal[4]
    d: UpdateVoiceStateData


# https://discord.com/developers/docs/topics/gateway-events#update-presence


@final
class PartialActivityData(TypedDict):
    name: str
    type: Literal[0, 1, 2, 3, 4, 5]
    url: NotRequired[str]


@final
class UpdatePresenceData(TypedDict):
    since: Optional[int]
    activities: List[PartialActivityData]
    status: Literal['online', 'idle', 'dnd', 'invisible']
    afk: bool


@final
class UpdatePresenceCommand(TypedDict):
    op: Literal[3]
    d: UpdatePresenceData


# https://discord.com/developers/docs/topics/gateway-events#hello


@final
class HelloData(TypedDict):
    heartbeat_interval: int


@final
class HelloEvent(TypedDict):
    op: Literal[10]
    d: HelloData
    s: None
    t: None


# https://discord.com/developers/docs/topics/gateway-events#ready


@final
class PartialApplicationData(TypedDict):
    id: Snowflake
    flags: int


@final
class ReadyData(TypedDict):
    v: int
    user: UserData
    guilds: List[UnavailableGuildData]
    session_id: str
    resume_gateway_url: str
    shard: NotRequired[Union[Tuple[int, int], List[int]]]
    application: PartialApplicationData


ReadyEvent = GenericDispatchEvent[Literal['READY'], ReadyData]


# https://discord.com/developers/docs/topics/gateway-events#resumed


@final
class ResumedData(TypedDict):
    ...  # It only has an undocumented _trace field


ResumedEvent = GenericDispatchEvent[Literal['RESUMED'], ResumedData]


# https://discord.com/developers/docs/topics/gateway-events#reconnect


@final
class ReconnectEvent(TypedDict):
    op: Literal[7]
    d: None
    s: None
    t: None


# https://discord.com/developers/docs/topics/gateway-events#invalid-session


@final
class InvalidSessionEvent(TypedDict):
    op: Literal[9]
    d: bool
    s: None
    t: None

# https://discord.com/developers/docs/topics/gateway-events#get-gateway-example-response


@final
class GetGatewayData(TypedDict):
    url: str

# https://discord.com/developers/docs/topics/gateway-events#application-command-permissions-update


ApplicationCommandPermissionsUpdateData: TypeAlias = 'ApplicationCommandPermissionsData'


ApplicationCommandPermissionsUpdateEvent = GenericDispatchEvent[
    Literal['APPLICATION_COMMAND_PERMISSIONS_UPDATE'],
    ApplicationCommandPermissionsUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#auto-moderation-rule-create


AutoModerationRuleCreateData: TypeAlias = 'AutoModerationRuleData'


AutoModerationRuleCreateEvent = GenericDispatchEvent[
    Literal['AUTO_MODERATION_RULE_CREATE'],
    AutoModerationRuleCreateData
]


# https://discord.com/developers/docs/topics/gateway-events#auto-moderation-rule-update


AutoModerationRuleUpdateData: TypeAlias = 'AutoModerationRuleData'


AutoModerationRuleUpdateEvent = GenericDispatchEvent[
    Literal['AUTO_MODERATION_RULE_UPDATE'],
    AutoModerationRuleUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#auto-moderation-rule-delete


AutoModerationRuleDeleteData: TypeAlias = 'AutoModerationRuleData'


AutoModerationRuleDeleteEvent = GenericDispatchEvent[
    Literal['AUTO_MODERATION_RULE_DELETE'],
    AutoModerationRuleDeleteData
]


# https://discord.com/developers/docs/topics/gateway-events#auto-moderation-action-execution


@final
class AutoModerationActionExecutionData(TypedDict):
    guild_id: Snowflake
    action: AutoModerationActionData
    rule_id: Snowflake
    rule_trigger_type: AutoModerationTriggerTypes
    user_id: Snowflake
    channel_id: NotRequired[Snowflake]
    message_id: NotRequired[Snowflake]
    alert_system_message_id: NotRequired[Snowflake]
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
    'TextChannelData', 'NewsChannelData', 'VoiceChannelData', 'CategoryChannelData'
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


@final
class ThreadCreateData(TypedDict):
    id: Snowflake
    type: Literal[10, 11, 12]
    guild_id: NotRequired[Snowflake]
    name: str
    last_message_id: Optional[Snowflake]
    rate_limit_per_user: int
    owner_id: Snowflake
    parent_id: Optional[Snowflake]
    last_pin_timestamp: NotRequired[Optional[str]]
    message_count: int
    member_count: int
    thread_metadata: ThreadMetadataData
    member: NotRequired[ThreadMemberData]

    newly_created: bool  # Extra THREAD_CREATE field


ThreadCreateEvent = GenericDispatchEvent[Literal['THREAD_CREATE'], ThreadCreateData]


# https://discord.com/developers/docs/topics/gateway-events#thread-update


ThreadUpdateData: TypeAlias = 'ThreadChannelData'
ThreadUpdateEvent = GenericDispatchEvent[Literal['THREAD_UPDATE'], ThreadUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#thread-delete


@final
class ThreadDeleteData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    parent_id: Snowflake
    type: Literal[10, 11, 12]


ThreadDeleteEvent = GenericDispatchEvent[Literal['THREAD_DELETE'], ThreadDeleteData]


# https://discord.com/developers/docs/topics/gateway-events#thread-list-sync


@final
class ThreadListSyncData(TypedDict):
    guild_id: Snowflake
    channel_ids: NotRequired[List[Snowflake]]
    threads: List[ThreadChannelData]
    members: List[ThreadMemberData]


ThreadListSyncEvent = GenericDispatchEvent[Literal['THREAD_LIST_SYNC'], ThreadListSyncData]


# https://discord.com/developers/docs/topics/gateway-events#thread-member-update


@final
class ThreadMemberUpdateData(TypedDict):
    # 'id' and 'user_id' is only missing in the GUILD_CREATE event, so we know
    # that they are present in this event (hence the missing NotRequired
    # compared to ThreadMemberData).
    id: Snowflake
    user_id: Snowflake
    guild_id: Snowflake
    join_timestamp: str
    flags: int


ThreadMemberUpdateEvent = GenericDispatchEvent[
    Literal['THREAD_MEMBER_UPDATE'], ThreadMemberUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#thread-members-update


@final
class ThreadMembersUpdateData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    member_count: int
    added_members: NotRequired[List[ThreadMemberData]]
    removed_member_ids: NotRequired[List[Snowflake]]


ThreadMembersUpdateEvent = GenericDispatchEvent[
    Literal['THREAD_MEMBERS_UPDATE'], ThreadMembersUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#channel-pins-update


@final
class ChannelPinsUpdateData(TypedDict):
    guild_id: NotRequired[Snowflake]
    channel_id: Snowflake
    last_pin_timestamp: NotRequired[Optional[str]]


ChannelPinsUpdateEvent = GenericDispatchEvent[
    Literal['CHANNEL_PINS_UPDATE'], ChannelPinsUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-create


@final
class GuildCreateData(TypedDict):
    id: str
    name: str
    icon: Optional[str]
    icon_hash: NotRequired[Optional[str]]
    splash: Optional[str]
    discovery_splash: Optional[str]
    owner: NotRequired[bool]
    owner_id: str
    permissions: NotRequired[str]
    afk_channel_id: Optional[str]
    afk_timeout: int
    widget_enabled: NotRequired[bool]
    widget_channel_id: NotRequired[Optional[str]]
    verification_level: Literal[0, 1, 2, 3, 4]
    default_message_notifications: Literal[0, 1]
    explicit_content_filter: Literal[0, 1, 2]
    roles: List[RoleData]
    emojis: List[EmojiData]
    features: List[GuildFeaturesData]
    mfa_level: Literal[0, 1]
    application_id: Optional[str]
    system_channel_id: Optional[str]
    system_channel_flags: int
    rules_channel_id: Optional[str]
    max_presences: NotRequired[Optional[int]]
    max_members: NotRequired[int]
    vanity_url_code: Optional[str]
    description: Optional[str]
    banner: Optional[str]
    premium_tier: Literal[0, 1, 2, 3]
    premium_subscription_count: NotRequired[int]
    preferred_locale: Locales
    public_updates_channel_id: Optional[str]
    max_video_channel_users: NotRequired[int]
    approximate_member_count: NotRequired[int]
    approximate_presence_count: NotRequired[int]
    welcome_screen: NotRequired[WelcomeScreenData]
    nsfw_level: Literal[0, 1, 2, 3]
    stickers: NotRequired[List[StickerData]]
    premium_progress_bar_enabled: bool

    # Extra GUILD_CREATE fields
    joined_at: str
    large: bool
    unavailable: bool
    member_count: int
    voice_states: List[VoiceStateData]
    members: List[GuildMemberData]
    channels: List[_GuildChannelData]
    threads: List[ThreadChannelData]
    presences: List[UpdatePresenceData]
    stage_instances: List[StageInstanceData]
    guild_scheduled_events: List[GuildScheduledEventData]


GuildCreateEvent = GenericDispatchEvent[Literal['GUILD_CREATE'], GuildCreateData]


# https://discord.com/developers/docs/topics/gateway-events#guild-update


GuildUpdateData: TypeAlias = 'GuildData'
GuildUpdateEvent = GenericDispatchEvent[Literal['GUILD_UPDATE'], GuildUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#guild-delete


GuildDeleteData: TypeAlias = 'UnavailableGuildData'
GuildDeleteEvent = GenericDispatchEvent[Literal['GUILD_DELETE'], 'GuildDeleteData']


# https://discord.com/developers/docs/topics/gateway-events#guild-audit-log-entry-create


GuildAuditLogEntryCreateData: TypeAlias = 'AuditLogEntryData'
GuildAuditLogEntryCreateEvent = GenericDispatchEvent[
    Literal['GUILD_AUDIT_LOG_ENTRY_CREATE'],
    'AuditLogEntryData'
]


# https://discord.com/developers/docs/topics/gateway-events#guild-ban-add


@final
class GuildBanAddData(TypedDict):
    guild_id: Snowflake
    user: UserData


GuildBanAddEvent = GenericDispatchEvent[Literal['GUILD_BAN_ADD'], GuildBanAddData]


# https://discord.com/developers/docs/topics/gateway-events#guild-ban-remove


@final
class GuildBanRemoveData(TypedDict):
    guild_id: Snowflake
    user: UserData


GuildBanRemoveEvent = GenericDispatchEvent[Literal['GUILD_BAN_REMOVE'], GuildBanRemoveData]


# https://discord.com/developers/docs/topics/gateway-events#guild-emojis-update


@final
class GuildEmojisUpdateData(TypedDict):
    guild_id: Snowflake
    emojis: List[EmojiData]


GuildEmojisUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_EMOJIS_UPDATE'], GuildEmojisUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-stickers-update


@final
class GuildStickersUpdateData(TypedDict):
    guild_id: Snowflake
    stickers: List[StickerData]


GuildStickersUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_STICKERS_UPDATE'], GuildStickersUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-integrations-update


@final
class GuildIntergrationsUpdateData(TypedDict):
    guild_id: Snowflake


GuildIntergrationsUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_INTEGRATIONS_UPDATE'], GuildIntergrationsUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-member-add


@final
class GuildMemberAddData(TypedDict):
    user: UserData  # Always present in GUILD_MEMBER_ADD events
    nick: NotRequired[Optional[str]]
    avatar: NotRequired[Optional[str]]
    roles: List[Snowflake]
    joined_at: str
    premium_since: NotRequired[Optional[str]]
    deaf: bool
    mute: bool
    pending: NotRequired[bool]
    permissions: NotRequired[str]

    guild_id: Snowflake  # Extra field


GuildMemberAddEvent = GenericDispatchEvent[Literal['GUILD_MEMBER_ADD'], GuildMemberAddData]


# https://discord.com/developers/docs/topics/gateway-events#guild-member-remove


@final
class GuildMemberRemoveData(TypedDict):
    user: UserData
    guild_id: Snowflake


GuildMemberRemoveEvent = GenericDispatchEvent[
    Literal['GUILD_MEMBER_REMOVE'], GuildMemberRemoveData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-member-update


@final
class GuildMemberUpdateData(TypedDict):
    guild_id: Snowflake
    roles: List[Snowflake]
    user: UserData
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


@final
class GuildMembersChunkData(TypedDict):
    guild_id: Snowflake
    members: List[GuildMemberData]
    chunk_index: int
    chunk_count: int
    not_found: NotRequired[List[Snowflake]]
    presences: NotRequired[List[PresenceUpdateData]]
    nonce: NotRequired[str]


GuildMembersChunkEvent = GenericDispatchEvent[
    Literal['GUILD_MEMBERS_CHUNK'], GuildMembersChunkData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-role-create


@final
class GuildRoleCreateData(TypedDict):
    guild_id: Snowflake
    role: RoleData


GuildRoleCreateEvent = GenericDispatchEvent[Literal['GUILD_ROLE_CREATE'], GuildRoleCreateData]


# https://discord.com/developers/docs/topics/gateway-events#guild-role-update


@final
class GuildRoleUpdateData(TypedDict):
    guild_id: Snowflake
    role: RoleData


GuildRoleUpdateEvent = GenericDispatchEvent[Literal['GUILD_ROLE_UPDATE'], GuildRoleUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#guild-role-delete


@final
class GuildRoleDeleteData(TypedDict):
    guild_id: Snowflake
    role_id: Snowflake


GuildRoleDeleteEvent = GenericDispatchEvent[Literal['GUILD_ROLE_DELETE'], GuildRoleDeleteData]


# https://discord.com/developers/docs/topics/gateway-events#guild-scheduled-event-create


GuildScheduledEventCreateData: TypeAlias = 'GuildScheduledEventData'
GuildScheduledEventCreateEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_CREATE'], GuildScheduledEventCreateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-scheduled-event-update


GuildScheduledEventUpdateData: TypeAlias = 'GuildScheduledEventData'
GuildScheduledEventUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_UPDATE'], GuildScheduledEventUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-scheduled-event-delete


GuildScheduledEventDeleteData: TypeAlias = 'GuildScheduledEventData'
GuildScheduledEventDeleteEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_DELETE'], GuildScheduledEventDeleteData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-scheduled-event-user-add


@final
class GuildScheduledEventUserAddData(TypedDict):
    guild_scheduled_event_id: Snowflake
    user_id: Snowflake
    guild_id: Snowflake


GuildScheduledEventUserAddEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_USER_ADD'], GuildScheduledEventUserAddData
]


# https://discord.com/developers/docs/topics/gateway-events#guild-scheduled-event-user-remove


@final
class GuildScheduledEventUserRemoveData(TypedDict):
    guild_scheduled_event_id: Snowflake
    user_id: Snowflake
    guild_id: Snowflake


GuildScheduledEventUserRemoveEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_USER_REMOVE'], GuildScheduledEventUserRemoveData
]


# https://discord.com/developers/docs/topics/gateway-events#integrations


@final
class _StreamingIntegrationGuildData(TypedDict):
    id: Snowflake
    name: str
    type: Literal['twitch', 'youtube', 'discord']
    enabled: bool
    syncing: bool
    role_id: NotRequired[Snowflake]
    enable_emoticons: bool
    expire_behavior: IntegrationExpireBehaviors
    expire_grace_period: int
    user: UserData
    account: IntegrationAccountData
    synced_at: str
    subscriber_count: int
    revoked: bool
    application: IntegrationApplicationData

    guild_id: Snowflake


@final
class _DiscordIntegrationGuildData(TypedDict):
    id: Snowflake
    name: str
    type: Literal['discord']
    enabled: bool
    account: IntegrationAccountData
    application: NotRequired[IntegrationApplicationData]

    guild_id: Snowflake


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


@final
class IntegrationDeleteData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    application_id: NotRequired[Snowflake]


IntegrationDeleteEvent = GenericDispatchEvent[
    Literal['INTEGRATION_DELETE'], IntegrationDeleteData
]


# https://discord.com/developers/docs/topics/gateway-events#invite-create


@final
class InviteCreateData(TypedDict):
    channel_id: Snowflake
    code: str
    created_at: str
    guild_id: NotRequired[Snowflake]
    inviter: NotRequired[UserData]
    max_age: int
    max_uses: int
    target_type: NotRequired[Literal[1, 2]]
    target_user: NotRequired[UserData]
    target_application: NotRequired[ApplicationData]
    temporary: bool
    uses: int


InviteCreateEvent = GenericDispatchEvent[Literal['INVITE_CREATE'], InviteCreateData]


# https://discord.com/developers/docs/topics/gateway-events#invite-delete


@final
class InviteDeleteData(TypedDict):
    channel_id: Snowflake
    guild_id: NotRequired[Snowflake]
    code: str


InviteDeleteEvent = GenericDispatchEvent[Literal['INVITE_DELETE'], InviteDeleteData]


# https://discord.com/developers/docs/topics/gateway-events#message-create


MessageCreateData: TypeAlias = 'MessageData'
MessageCreateEvent = GenericDispatchEvent[Literal['MESSAGE_CREATE'], MessageCreateData]


# https://discord.com/developers/docs/topics/gateway-events#message-update


MessageUpdateData: TypeAlias = 'MessageData'
MessageUpdateEvent = GenericDispatchEvent[Literal['MESSAGE_UPDATE'], MessageUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#message-delete


@final
class MessageDeleteData(TypedDict):
    id: Snowflake
    channel_id: Snowflake
    guild_id: NotRequired[Snowflake]


MessageDeleteEvent = GenericDispatchEvent[Literal['MESSAGE_DELETE'], MessageDeleteData]


# https://discord.com/developers/docs/topics/gateway-events#message-delete-bulk


@final
class MessageDeleteBulkData(TypedDict):
    ids: List[Snowflake]
    channel_id: Snowflake
    guild_id: NotRequired[Snowflake]


MessageDeleteBulkEvent = GenericDispatchEvent[
    Literal['MESSAGE_DELETE_BULK'], MessageDeleteBulkData
]


# https://discord.com/developers/docs/topics/gateway-events#message-reaction-add


@final
class MessageReactionAddData(TypedDict):
    user_id: Snowflake
    channel_id: Snowflake
    message_id: Snowflake
    guild_id: NotRequired[Snowflake]
    member: NotRequired[GuildMemberData]
    emoji: EmojiData


MessageReactionAddEvent = GenericDispatchEvent[
    Literal['MESSAGE_REACTION_ADD'], MessageReactionAddData
]


# https://discord.com/developers/docs/topics/gateway-events#message-reaction-remove


@final
class MessageReactionRemoveData(TypedDict):
    user_id: Snowflake
    channel_id: Snowflake
    message_id: Snowflake
    guild_id: NotRequired[Snowflake]
    emoji: EmojiData


MessageReactionRemoveEvent = GenericDispatchEvent[
    Literal['MESSAGE_REACTION_REMOVE'], MessageReactionRemoveData
]


# https://discord.com/developers/docs/topics/gateway-events#message-reaction-remove-all


@final
class MessageReactionRemoveAllData(TypedDict):
    channel_id: Snowflake
    message_id: Snowflake
    guild_id: NotRequired[Snowflake]


MessageReactionRemoveAllEvent = GenericDispatchEvent[
    Literal['MESSAGE_REACTION_REMOVE_ALL'], MessageReactionRemoveAllData
]


# https://discord.com/developers/docs/topics/gateway-events#message-reaction-remove-emoji


@final
class MessageReactionRemoveEmojiData(TypedDict):
    channel_id: Snowflake
    guild_id: NotRequired[Snowflake]
    message_id: Snowflake
    emoji: EmojiData


MessageReactionRemoveEmojiEvent = GenericDispatchEvent[
    Literal['MESSAGE_REACTION_REMOVE_EMOJI'], MessageReactionRemoveEmojiData
]


# https://discord.com/developers/docs/topics/gateway-events#presence-update


@final
class PresenceUpdateData(TypedDict):
    user: UserData
    guild_id: Snowflake
    status: Literal['idle', 'dnd', 'online', 'offline']
    activities: List[ActivityData]
    client_status: ClientStatusData


@final
class ClientStatusData(TypedDict):
    desktop: NotRequired[str]
    mobile: NotRequired[str]
    web: NotRequired[str]


# https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-structure


@final
class ActivityData(TypedDict):
    name: str
    type: Literal[0, 1, 2, 3, 4, 5]
    url: NotRequired[Optional[str]]
    created_at: int
    timestamps: NotRequired[ActivityTimestampsData]
    application_id: NotRequired[Snowflake]
    details: NotRequired[Optional[str]]
    state: NotRequired[Optional[str]]
    emoji: NotRequired[Optional[ActivityEmojiData]]
    party: NotRequired[Optional[ActivityPartyData]]
    assets: NotRequired[ActivityAssetsData]
    secrets: NotRequired[ActivitySecretsData]
    instance: NotRequired[bool]
    flags: NotRequired[int]
    buttons: NotRequired[List[ActivityButtonData]]


@final
class ActivityTimestampsData(TypedDict):
    start: NotRequired[int]
    end: NotRequired[int]


@final
class ActivityEmojiData(TypedDict):
    name: str
    id: NotRequired[Snowflake]
    animated: NotRequired[bool]


@final
class ActivityPartyData(TypedDict):
    id: NotRequired[str]
    size: NotRequired[Union[Tuple[int, int], List[int]]]


@final
class ActivityAssetsData(TypedDict):
    large_image: NotRequired[str]
    large_text: NotRequired[str]
    small_image: NotRequired[str]
    small_test: NotRequired[str]


@final
class ActivitySecretsData(TypedDict):
    join: NotRequired[str]
    spectate: NotRequired[str]
    match: NotRequired[str]


@final
class ActivityButtonData(TypedDict):
    label: str
    url: str


# https://discord.com/developers/docs/topics/gateway-events#typing-start


@final
class TypingStartData(TypedDict):
    channel_id: Snowflake
    guild_id: NotRequired[Snowflake]
    user_id: Snowflake
    timestamp: int
    member: NotRequired[GuildMemberData]


TypingStartEvent = GenericDispatchEvent[Literal['TYPING_START'], TypingStartData]


# https://discord.com/developers/docs/topics/gateway-events#user-update


UserUpdateData: TypeAlias = 'UserData'
UserUpdateEvent = GenericDispatchEvent[Literal['USER_UPDATE'], UserUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#voice-state-update


VoiceStateUpdateData: TypeAlias = 'VoiceStateData'
VoiceStateUpdateEvent = GenericDispatchEvent[
    Literal['VOICE_STATUS_UPDATE'], VoiceStateUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#voice-server-update


@final
class VoiceServerUpdateData(TypedDict):
    token: str
    guild_id: Snowflake
    endpoint: Optional[str]


VoiceServerUpdateEvent = GenericDispatchEvent[
    Literal['VOICE_SERVER_UPDATE'], VoiceServerUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#webhooks-update


@final
class WebhooksUpdateData(TypedDict):
    guild_id: Snowflake
    channel_id: Snowflake


WebhooksUpdateEvent = GenericDispatchEvent[Literal['WEBHOOKS_UPDATE'], WebhooksUpdateData]


# https://discord.com/developers/docs/topics/gateway-events#interaction-create


InteractionCreateData: TypeAlias = 'InteractionData'
InteractionCreateEvent = GenericDispatchEvent[
    Literal['INTERACTION_CREATE'], InteractionCreateData
]


# https://discord.com/developers/docs/topics/gateway-events#stage-instance-create


StageInstanceCreateData: TypeAlias = 'StageInstanceData'
StageInstanceCreateEvent = GenericDispatchEvent[
    Literal['STAGE_INSTANCE_CREATE'], StageInstanceCreateData
]


# https://discord.com/developers/docs/topics/gateway-events#stage-instance-update


StageInstanceUpdateData: TypeAlias = 'StageInstanceData'
StageInstanceUpdateEvent = GenericDispatchEvent[
    Literal['STAGE_INSTANCE_UPDATE'], StageInstanceUpdateData
]


# https://discord.com/developers/docs/topics/gateway-events#stage-instance-delete


StageInstanceDeleteData: TypeAlias = 'StageInstanceData'
StageInstanceDeleteEvent = GenericDispatchEvent[
    Literal['STAGE_INSTANCE_DELETE'], StageInstanceDeleteData
]


# https://discord.com/developers/docs/topics/gateway-events#get-gateway-bot-json-response


@final
class GetGatewayBotData(TypedDict):
    url: str
    shards: int
    session_start_limit: SessionStartLimitData


# https://discord.com/developers/docs/topics/gateway#session-start-limit-object


@final
class SessionStartLimitData(TypedDict):
    total: int
    remaining: int
    reset_after: int
    max_concurrency: int


# Generalized unions for the typings in this file


DispatchEvent = GenericDispatchEvent[str, Dict[str, Any]]


GatewayEvent = Union[
    HeartbeatACKEvent, HelloEvent, ReadyEvent, ResumedEvent, DispatchEvent,
    ReconnectEvent, InvalidSessionEvent,
]


GatewayCommand = Union[
    IdentifyCommand, ResumeCommand, HeartbeatCommand, RequestGuildMembersCommand,
    UpdateVoiceStateCommand
]
