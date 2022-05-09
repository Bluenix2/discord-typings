from __future__ import annotations

from typing import (
    TYPE_CHECKING, Any, Dict, List, Optional, Sequence, Tuple, Union
)

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from .resources import UnavailableGuildData, UserData
    from .shared import Snowflake

__all__ = (
    'HeartbeatACKData', 'IdentifyCommand', 'ResumeCommand', 'HeartbeatCommand',
    'RequestGuildMembersCommand', 'VoiceUpdateCommand',
    'UpdatePresenceCommand', 'HelloEvent', 'ReadyEvent', 'DispatchEvent',
    'ResumedEvent', 'ReconnectEvent', 'InvalidSessionEvent',
    'GetGatewayBotData', 'GatewayEvent',
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


# The leading dollar sign makes this an invalid attribute in Python so we need
# to use this way of defining typed dicts.
IdentifyConnectionProperties = final(TypedDict(
    'IdentifyConnectionProperties',
    {
        '$os': str,
        '$browser': str,
        '$device': str
    }
))


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
    user_ids: NotRequired[Sequence[Snowflake]]
    nonce: NotRequired[str]


@final
class _UserIDsRequestMembersCommand(TypedDict):
    guild_id: Snowflake
    presences: NotRequired[bool]
    user_ids: Sequence[Snowflake]
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
    activities: Sequence[ActivityData]
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
    guilds: Sequence[UnavailableGuildData]
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


GatewayEvent = Union[
    HeartbeatACKData, HelloEvent, ReadyEvent, ResumedEvent, DispatchEvent,
    ReconnectEvent, InvalidSessionEvent,
]
