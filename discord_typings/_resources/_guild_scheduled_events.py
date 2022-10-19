from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from .._reference import Snowflake
    from ._guild import GuildMemberData
    from ._user import UserData

__all__ = (
    'GuildScheduledEventData', 'GuildScheduledEventPrivacyLevels', 'GuildScheduledEventStatus',
    'GuildScheduledEventEntityTypes', 'GuildScheduledEventEntityMetadataData',
    'GuildScheduledEventUserData'
)


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-structure


class GuildScheduledEventBase(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    creator_id: Snowflake
    name: str
    description: NotRequired[Optional[str]]
    scheduled_start_time: str
    privacy_level: GuildScheduledEventPrivacyLevels
    status: GuildScheduledEventStatus
    entity_type: GuildScheduledEventEntityTypes
    entity_id: Optional[Snowflake]
    creator: UserData
    user_count: NotRequired[int]
    image: NotRequired[Optional[str]]


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
    entity_metadata: GuildScheduledEventEntityMetadataData
    scheduled_end_time: str


GuildScheduledEventData = Union[
    StageGuildScheduledEventData,
    VoiceGuildScheduledEventData,
    ExternalGuildScheduledEventData
]


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-privacy-level


GuildScheduledEventPrivacyLevels = Literal[2]


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-entity-types


GuildScheduledEventEntityTypes = Literal[1, 2, 3]


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-status


GuildScheduledEventStatus = Literal[1, 2, 3, 4]


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-entity-metadata


@final
class GuildScheduledEventEntityMetadataData(TypedDict):
    location: NotRequired[str]


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-user-object-guild-scheduled-event-user-structure


@final
class GuildScheduledEventUserData(TypedDict):
    guild_scheduled_event_id: Snowflake
    user: UserData
    member: NotRequired[GuildMemberData]
