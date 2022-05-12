from __future__ import annotations

from typing import (
    TYPE_CHECKING, Any, Dict, Generic, List, Mapping, Optional, Tuple, TypeVar,
    Union
)

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict, final

if TYPE_CHECKING:
    from .interactions import ApplicationCommandPermissionsData
    from .resources import (
        CategoryChannelData, EmojiData, GuildData, GuildMemberData,
        GuildScheduledEventData, NewsChannelData, RoleData, StickerData,
        TextChannelData, ThreadChannelData, ThreadMemberData, ThreadMetadata,
        UnavailableGuildData, UserData, VoiceChannelData
    )
    from .shared import Snowflake

__all__ = (
    'HeartbeatACKEvent', 'IdentifyData', 'IdentifyConnectionProperties', 'IdentifyCommand',
    'ResumeData', 'ResumeCommand', 'HeartbeatCommand', 'RequestGuildMembersData',
    'RequestGuildMembersCommand', 'VoiceUpdateData', 'VoiceUpdateCommand', 'ActivityData',
    'UpdatePresenceData', 'UpdatePresenceCommand', 'HelloData', 'HelloEvent',
    'PartialApplicationData', 'ReadyData', 'ReadyEvent', 'ResumedData', 'ResumedEvent',
    'ReconnectEvent', 'InvalidSessionEvent', 'ApplicationCommandPermissionsUpdateData',
    'ApplicationCommandPermissionsUpdateEvent', 'ChannelCreateData', 'ChannelCreateEvent',
    'ChannelUpdateData', 'ChannelUpdateEvent', 'ChannelDeleteData', 'ChannelDeleteEvent',
    'ThreadCreateData', 'ThreadCreateEvent', 'ThreadUpdateData', 'ThreadUpdateEvent',
    'ThreadDeleteData', 'ThreadDeleteEvent', 'ThreadListSyncData', 'ThreadListSyncEvent',
    'ThreadMemberUpdateData', 'ThreadMemberUpdateEvent', 'ThreadMembersUpdateData',
    'ThreadMembersUpdateEvent', 'ChannelPinsUpdateData', 'ChannelPinsUpdateEvent',
    'GetGatewayData', 'GetGatewayBotData', 'GatewayEvent',
)


_D = TypeVar('_D', bound='Mapping[str, Any]')
_T = TypeVar('_T', bound='str')  # Literal


@final
class GenericDispatchEvent(TypedDict, Generic[_T, _D]):
    """Helper generic TypedDict for annotating dispatch events.

    This should generally not be used, and does not necessarily represent any
    one payload from Discord. Consider this private as it is not exposed under
    the `discord_typings` namespace; use the public non-generic versions.

    The reason this doesn't have a leading underscore is to look nicer when
    previewed in editors and IDEs.
    """
    op: Literal[0]
    d: _D
    s: int
    t: _T


# https://discord.com/developers/docs/topics/gateway#heartbeating-example-gateway-heartbeat-ack


@final
class HeartbeatACKEvent(TypedDict):
    op: Literal[11]


# https://discord.com/developers/docs/topics/gateway#identify


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


# https://discord.com/developers/docs/topics/gateway#resume


@final
class ResumeData(TypedDict):
    token: str
    session_id: str
    seq: int


@final
class ResumeCommand(TypedDict):
    op: Literal[6]
    d: ResumeData


# https://discord.com/developers/docs/topics/gateway#heartbeat


@final
class HeartbeatCommand(TypedDict):
    op: Literal[1]
    d: Optional[int]


# https://discord.com/developers/docs/topics/gateway#request-guild-members


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


# https://discord.com/developers/docs/topics/gateway#update-voice-state


@final
class VoiceUpdateData(TypedDict):
    guild_id: Snowflake
    channel_id: Optional[Snowflake]
    self_mute: bool
    self_deaf: bool


@final
class VoiceUpdateCommand(TypedDict):
    op: Literal[4]
    d: VoiceUpdateData


# https://discord.com/developers/docs/topics/gateway#update-presence


@final
class ActivityData(TypedDict):
    name: str
    type: Literal[0, 1, 2, 3, 4, 5]
    url: NotRequired[str]


@final
class UpdatePresenceData(TypedDict):
    since: Optional[int]
    activities: List[ActivityData]
    status: Literal['online', 'idle', 'dnd', 'invisible']
    afk: bool


@final
class UpdatePresenceCommand(TypedDict):
    op: Literal[3]
    d: UpdatePresenceData


# https://discord.com/developers/docs/topics/gateway#hello


@final
class HelloData(TypedDict):
    heartbeat_interval: int


@final
class HelloEvent(TypedDict):
    op: Literal[10]
    d: HelloData
    s: None
    t: None


# https://discord.com/developers/docs/topics/gateway#ready


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
    shard: NotRequired[Union[Tuple[int, int], List[int]]]
    application: PartialApplicationData


ReadyEvent = GenericDispatchEvent[Literal['READY'], ReadyData]


# https://discord.com/developers/docs/topics/gateway#resumed


@final
class ResumedData(TypedDict):
    ...  # It only has an undocumented _trace field


ResumedEvent = GenericDispatchEvent[Literal['RESUMED'], ResumedData]


# https://discord.com/developers/docs/topics/gateway#reconnect


@final
class ReconnectEvent(TypedDict):
    op: Literal[7]
    d: None
    s: None
    t: None


# https://discord.com/developers/docs/topics/gateway#invalid-session


@final
class InvalidSessionEvent(TypedDict):
    op: Literal[9]
    d: bool
    s: None
    t: None

# https://discord.com/developers/docs/topics/gateway#get-gateway-example-response


@final
class GetGatewayData(TypedDict):
    url: str

# https://discord.com/developers/docs/topics/gateway#application-command-permissions-update


ApplicationCommandPermissionsUpdateData: TypeAlias = 'ApplicationCommandPermissionsData'


ApplicationCommandPermissionsUpdateEvent = GenericDispatchEvent[
    Literal['APPLICATION_COMMAND_PERMISSIONS_UPDATE'],
    ApplicationCommandPermissionsUpdateData
]


# https://discord.com/developers/docs/topics/gateway#channels


# Utility for the events below
_GuildChannelData = Union[
    'TextChannelData', 'NewsChannelData', 'VoiceChannelData', 'CategoryChannelData'
]


# https://discord.com/developers/docs/topics/gateway#channel-create


ChannelCreateData = _GuildChannelData
ChannelCreateEvent = GenericDispatchEvent[Literal['CHANNEL_CREATE'], ChannelCreateData]


# https://discord.com/developers/docs/topics/gateway#channel-update


ChannelUpdateData = _GuildChannelData
ChannelUpdateEvent = GenericDispatchEvent[Literal['CHANNEL_UPDATE'], ChannelUpdateData]


# https://discord.com/developers/docs/topics/gateway#channel-delete


ChannelDeleteData = _GuildChannelData
ChannelDeleteEvent = GenericDispatchEvent[Literal['CHANNEl_DELETE'], ChannelDeleteData]


# https://discord.com/developers/docs/topics/gateway#thread-create


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
    thread_metadata: ThreadMetadata
    member: NotRequired[ThreadMemberData]

    newly_created: bool  # Extra THREAD_CREATE field


ThreadCreateEvent = GenericDispatchEvent[Literal['THREAD_CREATE'], ThreadCreateData]


# https://discord.com/developers/docs/topics/gateway#thread-update


ThreadUpdateData: TypeAlias = 'ThreadChannelData'
ThreadUpdateEvent = GenericDispatchEvent[Literal['THREAD_UPDATE'], ThreadUpdateData]


# https://discord.com/developers/docs/topics/gateway#thread-delete


@final
class ThreadDeleteData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    parent_id: Snowflake
    type: Literal[10, 11, 12]


ThreadDeleteEvent = GenericDispatchEvent[Literal['THREAD_DELETE'], ThreadDeleteData]


# https://discord.com/developers/docs/topics/gateway#thread-list-sync


@final
class ThreadListSyncData(TypedDict):
    guild_id: Snowflake
    channel_ids: NotRequired[List[Snowflake]]
    threads: List[ThreadChannelData]
    members: List[ThreadMemberData]


ThreadListSyncEvent = GenericDispatchEvent[Literal['THREAD_LIST_SYNC'], ThreadListSyncData]


# https://discord.com/developers/docs/topics/gateway#thread-member-update


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


# https://discord.com/developers/docs/topics/gateway#thread-members-update


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


# https://discord.com/developers/docs/topics/gateway#channel-pins-update


@final
class ChannelPinsUpdateData(TypedDict):
    guild_id: NotRequired[Snowflake]
    channel_id: Snowflake
    last_pin_timestamp: NotRequired[Optional[str]]


ChannelPinsUpdateEvent = GenericDispatchEvent[
    Literal['CHANNEL_PINS_UPDATE'], ChannelPinsUpdateData
]


# https://discord.com/developers/docs/topics/gateway#guild-create


# TODO: ...


# https://discord.com/developers/docs/topics/gateway#guild-update


GuildUpdateData: TypeAlias = 'GuildData'
GuildUpdateEvent = GenericDispatchEvent[Literal['GUILD_UPDATE'], GuildUpdateData]


# https://discord.com/developers/docs/topics/gateway#guild-delete


GuildDeleteData: TypeAlias = 'UnavailableGuildData'
GuildDeleteEvent = GenericDispatchEvent[Literal['GUILD_DELETE'], 'GuildDeleteData']


# https://discord.com/developers/docs/topics/gateway#guild-ban-add


@final
class GuildBanAddData(TypedDict):
    guild_id: Snowflake
    user: UserData


GuildBanAddEvent = GenericDispatchEvent[Literal['GUILD_BAN_ADD'], GuildBanAddData]


# https://discord.com/developers/docs/topics/gateway#guild-ban-remove


@final
class GuildBanRemoveData(TypedDict):
    guild_id: Snowflake
    user: UserData


GuildBanRemoveEvent = GenericDispatchEvent[Literal['GUILD_BAN_REMOVE'], GuildBanRemoveData]


# https://discord.com/developers/docs/topics/gateway#guild-emojis-update


@final
class GuildEmojisUpdateData(TypedDict):
    guild_id: Snowflake
    emojis: List[EmojiData]


GuildEmojisUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_EMOJIS_UPDATE'], GuildEmojisUpdateData
]


# https://discord.com/developers/docs/topics/gateway#guild-stickers-update


@final
class GuildStickersUpdateData(TypedDict):
    guild_id: Snowflake
    stickers: List[StickerData]


GuildStickersUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_STICKERS_UPDATE'], GuildStickersUpdateData
]


# https://discord.com/developers/docs/topics/gateway#guild-integrations-update


@final
class GuildIntergrationsUpdateData(TypedDict):
    guild_id: Snowflake


GuildIntergrationsUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_INTEGRATIONS_UPDATE'], GuildIntergrationsUpdateData
]


# https://discord.com/developers/docs/topics/gateway#guild-member-add


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


# https://discord.com/developers/docs/topics/gateway#guild-member-remove


@final
class GuildMemberRemoveData(TypedDict):
    user: UserData
    guild_id: Snowflake


GuildMemberRemoveEvent = GenericDispatchEvent[
    Literal['GUILD_MEMBER_REMOVE'], GuildMemberRemoveData
]


# https://discord.com/developers/docs/topics/gateway#guild-member-update


@final
class GuildMemberUpdateData(TypedDict):
    guild_id: Snowflake
    roles: List[Snowflake]
    user: List[UserData]
    nick: NotRequired[Optional[str]]
    avatar: Optional[str]
    joined_at: Optional[str]
    premium_since: NotRequired[Optional[str]]
    deaf: NotRequired[bool]
    mute: NotRequired[bool]
    pending: NotRequired[bool]
    communication_disabled_until: NotRequired[Optional[str]]


GuildmemberUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_MEMBER_UPDATE'], GuildMemberUpdateData
]


# https://discord.com/developers/docs/topics/gateway#guild-members-chunk


@final
class GuildMembersChunkData(TypedDict):
    guild_id: Snowflake
    members: List[GuildMemberData]
    chunk_index: int
    chunk_count: int
    not_found: NotRequired[List[Snowflake]]
    presences: NotRequired[List[UpdatePresenceData]]
    nonce: NotRequired[str]


GuildMembersChunkEvent = GenericDispatchEvent[
    Literal['GUILD_MEMBERS_CHUNK'], GuildMembersChunkData
]


# https://discord.com/developers/docs/topics/gateway#guild-role-create


@final
class GuildRoleCreateData(TypedDict):
    guild_id: Snowflake
    role: RoleData


GuildRoleCreateEvent = GenericDispatchEvent[Literal['GUILD_ROLE_CREATE'], GuildRoleCreateData]


# https://discord.com/developers/docs/topics/gateway#guild-role-update


@final
class GuildRoleUpdateData(TypedDict):
    guild_id: Snowflake
    role: RoleData


GuildRoleUpdateEvent = GenericDispatchEvent[Literal['GUILD_ROLE_UPDATE'], GuildRoleUpdateData]


# https://discord.com/developers/docs/topics/gateway#guild-role-delete


@final
class GuildRoleDeleteData(TypedDict):
    guild_id: Snowflake
    role_id: Snowflake


GuildRoleDeleteEvent = GenericDispatchEvent[Literal['GUILD_ROLE_DELETE'], GuildRoleDeleteData]


# https://discord.com/developers/docs/topics/gateway#guild-scheduled-event-create


GuildScheduledEventCreateData: TypeAlias = 'GuildScheduledEventData'
GuildScheduledEventCreateEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_CREATE'], GuildScheduledEventCreateData
]


# https://discord.com/developers/docs/topics/gateway#guild-scheduled-event-update


GuildScheduledEventUpdateData: TypeAlias = 'GuildScheduledEventData'
GuildScheduledEventUpdateEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_UPDATE'], GuildScheduledEventUpdateData
]


# https://discord.com/developers/docs/topics/gateway#guild-scheduled-event-delete


GuildScheduledEventDeleteData: TypeAlias = 'GuildScheduledEventData'
GuildScheduledEventDeleteEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_DELETE'], GuildScheduledEventDeleteData
]


# https://discord.com/developers/docs/topics/gateway#guild-scheduled-event-user-add


@final
class GuildScheduledEventUserAddData(TypedDict):
    guild_scheduled_event_id: Snowflake
    user_id: Snowflake
    guild_id: Snowflake


GuildScheduledEventUserAddEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_USER_ADD'], GuildScheduledEventUserAddData
]


# https://discord.com/developers/docs/topics/gateway#guild-scheduled-event-user-remove


@final
class GuildScheduledEventUserRemoveData(TypedDict):
    guild_scheduled_event_id: Snowflake
    user_id: Snowflake
    guild_id: Snowflake


GuildScheduledEventUserRemoveEvent = GenericDispatchEvent[
    Literal['GUILD_SCHEDULED_EVENT_USER_REMOVE'], GuildScheduledEventUserRemoveData
]


# https://discord.com/developers/docs/topics/gateway#get-gateway-bot-json-response


@final
class GetGatewayBotData(TypedDict):
    url: str
    shards: int
    session_start_limit: SessionStartLimitData


# https://discord.com/developers/docs/topics/gateway#session-start-limit-object-session-start-limit-structure


@final
class SessionStartLimitData(TypedDict):
    total: int
    remaining: int
    reset_after: int
    max_concurrency: int


DispatchEvent = GenericDispatchEvent[str, Dict[str, Any]]


GatewayEvent = Union[
    HeartbeatACKEvent, HelloEvent, ReadyEvent, ResumedEvent, DispatchEvent,
    ReconnectEvent, InvalidSessionEvent,
]
