from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from .resources import UnavailableGuildData, UserData
    from .shared import Snowflake

__all__ = (
    'HeartbeatACKData', 'IdentifyCommand', 'ResumeCommand', 'HeartbeatCommand',
    'RequestGuildMembersCommand', 'VoiceUpdateCommand',
    'UpdatePresenceCommand', 'HelloEvent', 'ReadyEvent', 'DispatchEvent',
    'ResumedEvent', 'ReconnectEvent', 'InvalidSessionEvent',
    'GetGatewayData', 'GetGatewayBotData', 'GatewayEvent',
)


# https://discord.com/developers/docs/topics/gateway#heartbeating-example-gateway-heartbeat-ack


@final
class HeartbeatACKData(TypedDict):
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


@final
class RequestGuildMembersCommand(TypedDict):
    op: Literal[8]
    # This enforces the fact that 'limit' is required when 'query' is set.
    d: Union[_QueryRequestMembersCommand, _UserIDsRequestMembersCommand]


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


@final
class ReadyEvent(TypedDict):
    op: Literal[0]
    d: ReadyData
    s: int
    t: Literal['READY']


@final
class GenericDispatchData(TypedDict):
    op: Literal[0]
    d: Dict[str, Any]
    s: int
    t: str


DispatchEvent = Union[ReadyEvent, 'ResumedEvent', GenericDispatchData]


# https://discord.com/developers/docs/topics/gateway#resumed


@final
class ResumedEvent(TypedDict):
    op: Literal[0]
    d: Dict[str, Any]  # It only has an undocumented _trace field
    s: int
    t: Literal['RESUMED']


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


ApplicationCommandPermissionsUpdateData = ApplicationCommandPermissionsData


ApplicationCommandPermissionsUpdateEvent = GenericDispatchEvent[
    Literal['APPLICATION_COMMAND_PERMISSIONS_UPDATE'],
    ApplicationCommandPermissionsUpdateData
]


# https://discord.com/developers/docs/topics/gateway#channels


# Utility for the events below
_GuildChannelData = Union[
    TextChannelData, NewsChannelData, VoiceChannelData, CategoryChannelData
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


ThreadUpdateData = ThreadChannelData
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
    Literal['THREAD_MEMBER_UPDATE'], ThreadMemberData
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
