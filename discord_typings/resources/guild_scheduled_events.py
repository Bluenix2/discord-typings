from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from ..shared import Snowflake
    from .guild import GuildMemberData
    from .user import UserData

__all__ = (
    'GuildScheduledEventData', 'GuildScheduledEventEntityMetadata',
    'GuildScheduledEventUserData'
)


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-structure


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


@final
class StageGuildScheduledEventData(GuildScheduledEventBase):
    channel_id: Snowflake
    entity_metadata: None
    scheduled_end_time: NotRequired[str]


@final
class VoiceGuildScheduledEventData(GuildScheduledEventBase):
    channel_id: Snowflake
    entity_metadata: None
    scheduled_end_time: NotRequired[str]


@final
class ExternalGuildScheduledEventData(GuildScheduledEventBase):
    channel_id: None
    entity_metadata: GuildScheduledEventEntityMetadata
    scheduled_end_time: str


GuildScheduledEventData = Union[
    StageGuildScheduledEventData,
    VoiceGuildScheduledEventData,
    ExternalGuildScheduledEventData
]


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-entity-metadata


@final
class GuildScheduledEventEntityMetadata(TypedDict):
    location: NotRequired[str]


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-user-object-guild-scheduled-event-user-structure


@final
class GuildScheduledEventUserData(TypedDict):
    guild_scheduled_event_id: Snowflake
    user: UserData
    memer: NotRequired[GuildMemberData]
