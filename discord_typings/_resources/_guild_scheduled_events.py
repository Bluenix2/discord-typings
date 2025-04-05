from typing import List, Optional, Union

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'StageGuildScheduledEventData',
    'VoiceGuildScheduledEventData',
    'ExternalGuildScheduledEventData',
    'GuildScheduledEventData',
    'GuildScheduledEventPrivacyLevels',
    'GuildScheduledEventStatus',
    'GuildScheduledEventEntityTypes',
    'GuildScheduledEventEntityMetadataData',
    'GuildScheduledEventUserData',
    'GuildScheduledEventRecurrenceRuleData',
    'GuildScheduledEventRecurrenceRuleFrequency',
    'GuildScheduledEventRecurrenceRuleWeekday',
    'GuildScheduledEventRecurrenceRuleNWeekdayData',
    'GuildScheduledEventRecurrenceRuleMonth'
)


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-structure


class _GuildScheduledEventData(TypedDict):
    id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'
    creator_id: 'discord_typings.Snowflake'
    name: str
    description: NotRequired[Optional[str]]
    scheduled_start_time: str
    privacy_level: 'discord_typings.GuildScheduledEventPrivacyLevels'
    status: 'discord_typings.GuildScheduledEventStatus'
    entity_id: Optional['discord_typings.Snowflake']
    creator: 'discord_typings.UserData'
    user_count: NotRequired[int]
    image: NotRequired[Optional[str]]
    recurrence_rule: Optional['discord_typings.GuildScheduledEventRecurrenceRuleData']


class StageGuildScheduledEventData(_GuildScheduledEventData):
    entity_type: Literal[1]
    channel_id: 'discord_typings.Snowflake'
    entity_metadata: None
    scheduled_end_time: NotRequired[str]


class VoiceGuildScheduledEventData(_GuildScheduledEventData):
    entity_type: Literal[2]
    channel_id: 'discord_typings.Snowflake'
    entity_metadata: None
    scheduled_end_time: NotRequired[str]


class ExternalGuildScheduledEventData(_GuildScheduledEventData):
    entity_type: Literal[3]
    channel_id: None
    entity_metadata: 'discord_typings.GuildScheduledEventEntityMetadataData'
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


class GuildScheduledEventEntityMetadataData(TypedDict):
    location: NotRequired[str]


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-user-object


class GuildScheduledEventUserData(TypedDict):
    guild_scheduled_event_id: 'discord_typings.Snowflake'
    user: 'discord_typings.UserData'
    member: NotRequired['discord_typings.GuildMemberData']


# https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-recurrence-rule-object


# Technically this could be done, such that it's possible to exclude invalid
# combinations in the typing system, but it's too complicated I don't understand
class GuildScheduledEventRecurrenceRuleData(TypedDict):
    start: str
    end: Optional[str]
    frequency: 'discord_typings.GuildScheduledEventRecurrenceRuleFrequency'
    interval: int
    by_weekday: Optional[List['discord_typings.GuildScheduledEventRecurrenceRuleWeekday']]
    by_n_weekday: Optional[
        List['discord_typings.GuildScheduledEventRecurrenceRuleNWeekdayData']
    ]
    by_month: Optional[List['discord_typings.GuildScheduledEventRecurrenceRuleMonth']]
    by_month_day: Optional[List[int]]
    by_year_day: Optional[List[int]]
    count: Optional[int]


GuildScheduledEventRecurrenceRuleFrequency = Literal[
    0, 1, 2, 3
]


GuildScheduledEventRecurrenceRuleWeekday = Literal[
    0, 1, 2, 3, 4, 5, 6
]


class GuildScheduledEventRecurrenceRuleNWeekdayData(TypedDict):
    n: int
    day: 'discord_typings.GuildScheduledEventRecurrenceRuleWeekday'


GuildScheduledEventRecurrenceRuleMonth = Literal[
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
]
