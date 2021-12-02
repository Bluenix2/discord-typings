from __future__ import annotations

from typing import Literal, Optional, TypedDict, Union

from typing_extensions import NotRequired

from ..shared import Snowflake
from .user import UserData

__all__ = ('GuildScheduledEventData', 'GuildScheduledEventEntityMetadata')


class GuildScheduledEventBase(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    creator_id: Snowflake
    name: str
    description: NotRequired[str]
    scheduled_start_time: str
    privacy_level: Literal[2]
    status: Literal[1, 2, 3, 4]
    entity_type: Literal[1, 2, 3]
    entity_id: Optional[Snowflake]
    creator: UserData
    user_count: NotRequired[int]


class StageGuildScheduledEventData(GuildScheduledEventBase):
    channel_id: Snowflake
    entity_metadata: None
    scheduled_end_time: NotRequired[str]


class VoiceGuildScheduledEventData(GuildScheduledEventBase):
    channel_id: Snowflake
    entity_metadata: None
    scheduled_end_time: NotRequired[str]


class ExternalGuildScheduledEventData(GuildScheduledEventBase):
    channel_id: None
    entity_metadata: GuildScheduledEventEntityMetadata
    scheduled_end_time: str


GuildScheduledEventData = Union[
    StageGuildScheduledEventData,
    VoiceGuildScheduledEventData,
    ExternalGuildScheduledEventData
]


class GuildScheduledEventEntityMetadata(TypedDict):
    location: NotRequired[str]
