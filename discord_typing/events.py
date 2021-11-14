from typing import Dict, Iterable, Optional, Tuple

from typing_extensions import Literal, NotRequired, TypedDict


class HelloBody(TypedDict):
    heartbeat_interval: int


class HelloEvent(TypedDict):
    op: Literal[0]
    d: HelloBody


class ResumeData(TypedDict):
    token: str
    session_id: str
    seq: int


class ResumeEvent(TypedDict):
    op: Literal[6]
    d: ResumeData


class ActivityData(TypedDict):
    name: str
    type: Literal[0, 1, 2, 3, 4, 5]
    url: NotRequired[Optional[str]]


class PresenceData(TypedDict):
    since: Optional[int]
    status: Literal['online', 'dnd', 'idle', 'invisible', 'offline']
    activites: Iterable[ActivityData]
    afk: bool


class IdentifyData(TypedDict):
    token: str
    properties: Dict
    compress: NotRequired[bool]
    large_threshold: NotRequired[int]
    shard: NotRequired[Tuple[int, int]]
    intents: int
