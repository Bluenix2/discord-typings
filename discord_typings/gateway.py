from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from typing_extensions import Literal, NotRequired, TypedDict

from .resources import UnavailableGuildData, UserData
from .shared import Snowflake

__all__ = (
    'IdentifyCommand', 'ResumeCommand', 'HeartbeatCommand',
    'RequestGuildMembersCommand', 'VoiceUpdateCommand',
    'UpdatePresenceCommand', 'HelloEvent', 'ReadyEvent', 'DispatchEvent',
    'ReconnectEvent', 'InvalidSessionEvent', 'GetGatewayBotData'
)


class IdentifyData(TypedDict):
    token: str
    properties: IdentifyConnectionProperties
    compress: NotRequired[bool]
    large_threshold: NotRequired[int]
    shard: NotRequired[Union[Tuple[int, int], List[int]]]
    presence: UpdatePresenceData
    intents: int


# The leading dollar sign makes this an invalid attribute in Python so we need
# to use this way of defining typed dicts.
IdentifyConnectionProperties = TypedDict(
    'IdentifyConnectionProperties',
    {
        '$os': str,
        '$browser': str,
        '$device': str
    }
)


class IdentifyCommand(TypedDict):
    op: Literal[2]
    d: IdentifyData
    s: None
    t: None


class ResumeData(TypedDict):
    token: str
    session_id: str
    seq: int


class ResumeCommand(TypedDict):
    op: Literal[6]
    d: ResumeData
    s: None
    t: None


class HeartbeatCommand(TypedDict):
    op: Literal[1]
    d: Optional[int]
    s: None
    t: None


class _QueryRequestMembersCommand(TypedDict):
    guild_id: Snowflake
    query: str
    limit: int
    presences: NotRequired[bool]
    user_ids: NotRequired[Sequence[Snowflake]]
    nonce: NotRequired[str]


class _UserIDsRequstMembersCommand(TypedDict):
    guild_id: Snowflake
    presences: NotRequired[bool]
    user_ids: Sequence[Snowflake]
    nonce: NotRequired[str]


class RequestGuildMembersCommand(TypedDict):
    op: Literal[8]
    # This enforces the fact that 'limit' is required when 'query' is set.
    d: Union[_QueryRequestMembersCommand, _UserIDsRequstMembersCommand]
    s: None
    t: None


class VoiceUpdateData(TypedDict):
    guild_id: Snowflake
    channel_id: Optional[Snowflake]
    self_mute: bool
    self_deaf: bool


class VoiceUpdateCommand(TypedDict):
    op: Literal[4]
    d: VoiceUpdateData
    s: None
    t: None


class UpdatePresenceData(TypedDict):
    since: Optional[int]
    activities: Sequence[ActivityData]
    status: Literal['online', 'idle', 'dnd', 'invisible']
    afk: bool


class UpdatePresenceCommand(TypedDict):
    op: Literal[3]
    d: UpdatePresenceData
    s: None
    t: None


class HelloData(TypedDict):
    heartbeat_interval: int


class HelloEvent(TypedDict):
    op: Literal[10]
    d: HelloData
    s: None
    t: None


class ReadyData(TypedDict):
    v: int
    user: UserData
    guilds: Sequence[UnavailableGuildData]
    session_id: str
    shard: NotRequired[Union[Tuple[int, int], List[int]]]
    application: PartialApplicationData


class ReadyEvent(TypedDict):
    op: Literal[0]
    d: ReadyData
    s: int
    t: Literal['READY']


class _GenericDispatch(TypedDict):
    op: Literal[0]
    d: Dict[str, Any]
    s: int
    t: str


DispatchEvent = Union[ReadyEvent, _GenericDispatch]


class PartialApplicationData(TypedDict):
    id: Snowflake
    flags: int


class ReconnectEvent(TypedDict):
    op: Literal[7]
    d: None
    s: None
    t: None


class InvalidSessionEvent(TypedDict):
    op: Literal[9]
    d: bool
    s: None
    t: None


class ActivityData(TypedDict):
    name: str
    type: Literal[0, 1, 2, 3, 4, 5]
    url: NotRequired[str]


class GetGatewayBotData(TypedDict):
    url: str
    shard: int
    session_start_limit: SessionStartLimitData


class SessionStartLimitData(TypedDict):
    total: int
    remaining: int
    reset_after: int
    max_concurrency: int
