from typing import List, Union

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'KeywordAutoModerationRuleData',
    'SpamAutoModerationRuleData',
    'KeywordPresetAutoModerationRuleData',
    'MentionSpamAutoModerationRuleData',
    'AutoModerationRuleData',
    'AutoModerationTriggerTypes',
    'KeywordAutoModerationTriggerMetadata',
    'KeywordPresetAutoModerationTriggerMetadataData',
    'MentionSpamAutoModerationTriggerMetadataData',
    'EmptyAutoModerationTriggerMetadataData',
    'AutoModerationTriggerMetadataData',
    'AutoModerationKeywordPresetTypes',
    'AutoModerationEventTypes',
    'BlockMessageAutoModerationActionData',
    'SendAlertMessageAutoModerationActionData',
    'TimeoutAutoModerationActionData',
    'AutoModerationActionData',
    'AutoModerationActionTypes',
    'BlockmessageAutoModerationActionMetadataData',
    'SendAlertMessageAutoModerationActionMetadataData',
    'TimeoutAutoModerationActionMetadataData',
    'AutoModerationActionMetadataData',
)


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-auto-moderation-rule-structure


class _AutoModerationRuleData(TypedDict):
    id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'
    name: str
    creator_id: 'discord_typings.Snowflake'
    event_type: 'discord_typings.AutoModerationEventTypes'
    actions: List['discord_typings.AutoModerationActionData']
    enabled: bool
    exempt_roles: List['discord_typings.Snowflake']
    exempt_channels: List['discord_typings.Snowflake']


class KeywordAutoModerationRuleData(_AutoModerationRuleData):
    trigger_type: Literal[1]
    trigger_metadata: 'discord_typings.KeywordAutoModerationTriggerMetadata'


class SpamAutoModerationRuleData(_AutoModerationRuleData):
    trigger_type: Literal[3]
    trigger_metadata: 'discord_typings.EmptyAutoModerationTriggerMetadataData'


class KeywordPresetAutoModerationRuleData(_AutoModerationRuleData):
    trigger_type: Literal[4]
    trigger_metadata: 'discord_typings.KeywordPresetAutoModerationTriggerMetadataData'


class MentionSpamAutoModerationRuleData(_AutoModerationRuleData):
    trigger_type: Literal[5]
    trigger_metadata: 'discord_typings.MentionSpamAutoModerationTriggerMetadataData'


AutoModerationRuleData = Union[
    KeywordAutoModerationRuleData, KeywordPresetAutoModerationRuleData,
    SpamAutoModerationRuleData, MentionSpamAutoModerationRuleData
]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-trigger-types


AutoModerationTriggerTypes = Literal[1, 2, 3, 4]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-trigger-metadata


class KeywordAutoModerationTriggerMetadata(TypedDict):
    keyword_filter: List[str]
    regex_patterns: List[str]

    allow_list: List[str]


class KeywordPresetAutoModerationTriggerMetadataData(TypedDict):
    presets: List['discord_typings.AutoModerationKeywordPresetTypes']


class MentionSpamAutoModerationTriggerMetadataData(TypedDict):
    mention_total_limit: int
    mention_raid_protection_enabled: bool


class EmptyAutoModerationTriggerMetadataData(TypedDict):
    ...


AutoModerationTriggerMetadataData = Union[
    KeywordAutoModerationTriggerMetadata,
    KeywordPresetAutoModerationTriggerMetadataData,
    MentionSpamAutoModerationTriggerMetadataData,
    EmptyAutoModerationTriggerMetadataData,
]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-keyword-preset-types


AutoModerationKeywordPresetTypes = Literal[1, 2, 3]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-event-types


AutoModerationEventTypes = Literal[1]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-action-object-auto-moderation-action-structure


class BlockMessageAutoModerationActionData(TypedDict):
    type: Literal[1]
    metadata: NotRequired['discord_typings.BlockmessageAutoModerationActionMetadataData']


class SendAlertMessageAutoModerationActionData(TypedDict):
    type: Literal[2]
    metadata: 'discord_typings.SendAlertMessageAutoModerationActionMetadataData'


class TimeoutAutoModerationActionData(TypedDict):
    type: Literal[3]
    metadata: 'discord_typings.TimeoutAutoModerationActionMetadataData'


AutoModerationActionData = Union[
    BlockMessageAutoModerationActionData, SendAlertMessageAutoModerationActionData,
    TimeoutAutoModerationActionData
]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-action-object-action-types


AutoModerationActionTypes = Literal[1, 2, 3]


# https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-action-object-action-metadata


class BlockmessageAutoModerationActionMetadataData(TypedDict):
    custom_message: NotRequired[str]


class SendAlertMessageAutoModerationActionMetadataData(TypedDict):
    channel_id: 'discord_typings.Snowflake'


class TimeoutAutoModerationActionMetadataData(TypedDict):
    duration_seconds: int


AutoModerationActionMetadataData = Union[
    BlockmessageAutoModerationActionMetadataData,
    SendAlertMessageAutoModerationActionMetadataData,
    TimeoutAutoModerationActionMetadataData,
]
