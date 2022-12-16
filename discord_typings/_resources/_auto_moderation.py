from __future__ import annotations

from typing import List, Union

from typing_extensions import Literal, TypedDict, final

from .._reference import Snowflake

__all__ = [
    'AutoModerationRuleData', 'AutoModerationTriggerTypes',
    'AutoModerationTriggerMetadataData', 'AutoModerationKeywordPresetTypes',
    'AutoModerationEventTypes', 'AutoModerationActionData', 'AutoModerationActionTypes',

]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-auto-moderation-rule-structure


@final
class KeywordAutoModerationRuleData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    name: str
    creator_id: Snowflake
    event_type: AutoModerationEventTypes
    trigger_type: Literal[1]
    trigger_metadata: KeywordTriggerMetadataData
    actions: List[AutoModerationActionData]
    enabled: bool
    exempt_roles: List[Snowflake]
    exempt_channels: List[Snowflake]


@final
class SpamAutoModerationRuleData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    name: str
    creator_id: Snowflake
    event_type: AutoModerationEventTypes
    trigger_type: Literal[3]
    trigger_metadata: EmptyTriggerMetadataData
    actions: List[AutoModerationActionData]
    enabled: bool
    exempt_roles: List[Snowflake]
    exempt_channels: List[Snowflake]


@final
class KeywordPresetAutoModerationRuleData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    name: str
    creator_id: Snowflake
    event_type: AutoModerationEventTypes
    trigger_type: Literal[4]
    trigger_metadata: KeywordPresetTriggerMetadataData
    actions: List[AutoModerationActionData]
    enabled: bool
    exempt_roles: List[Snowflake]
    exempt_channels: List[Snowflake]


@final
class MentionSpamAutoModerationRuleData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    name: str
    creator_id: Snowflake
    event_type: Literal[5]
    trigger_metadata: MentionSpamTriggerMetadataData
    actions: List[AutoModerationActionData]
    enabled: bool
    exempt_roles: List[Snowflake]
    exempt_channels: List[Snowflake]


AutoModerationRuleData = Union[
    KeywordAutoModerationRuleData, KeywordPresetAutoModerationRuleData,
    SpamAutoModerationRuleData, MentionSpamAutoModerationRuleData
]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-trigger-types


AutoModerationTriggerTypes = Literal[1, 2, 3, 4]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-trigger-metadata


@final
class KeywordTriggerMetadataData(TypedDict):
    keyword_filter: List[str]
    allow_list: List[str]

    regex_patterns: List[str]


@final
class KeywordPresetTriggerMetadataData(TypedDict):
    presets: List[AutoModerationKeywordPresetTypes]


@final
class MentionSpamTriggerMetadataData(TypedDict):
    mention_total_limit: int


@final
class EmptyTriggerMetadataData(TypedDict):
    ...


AutoModerationTriggerMetadataData = Union[
    KeywordTriggerMetadataData, KeywordPresetTriggerMetadataData,
    MentionSpamTriggerMetadataData, EmptyTriggerMetadataData
]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-keyword-preset-types


AutoModerationKeywordPresetTypes = Literal[1, 2, 3]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-event-types


AutoModerationEventTypes = Literal[1]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-action-object-auto-moderation-action-structure


@final
class BlockMessageAutoModerationActionData(TypedDict):
    type: Literal[1]


@final
class SendAlertMessageAutoModerationActionData(TypedDict):
    type: Literal[2]
    metadata: SendAlertMessageAutoModerationActionMetadataData


@final
class TimeoutAutoModerationActionData(TypedDict):
    type: Literal[3]
    metadata: TimeoutAutoModerationActionMetadataData


AutoModerationActionData = Union[
    BlockMessageAutoModerationActionData, SendAlertMessageAutoModerationActionData,
    TimeoutAutoModerationActionData
]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-action-object-action-types


AutoModerationActionTypes = Literal[1, 2, 3]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-action-object-action-metadata


@final
class SendAlertMessageAutoModerationActionMetadataData(TypedDict):
    channel_id: Snowflake


@final
class TimeoutAutoModerationActionMetadataData(TypedDict):
    duration_seconds: int


AutoModerationActionMetadataData = Union[
    SendAlertMessageAutoModerationActionMetadataData, TimeoutAutoModerationActionMetadataData
]
