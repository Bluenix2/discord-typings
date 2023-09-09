from typing import Any, List, Optional

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'AuditLogData',
    'PartialIntegrationData',
    'AuditLogEntryData',
    'OptionalAuditLogEntryData',
    'AuditLogChangeData',
    'AuditLogEvents',
)


# https://discord.com/developers/docs/resources/audit-log#audit-log-object-audit-log-structure


class AuditLogData(TypedDict):
    application_commands: List['discord_typings.ApplicationCommandData']
    audit_log_entries: List['discord_typings.AuditLogEntryData']
    auto_moderation_rules: List['discord_typings.AutoModerationRuleData']
    guild_scheduled_events: List['discord_typings.GuildScheduledEventData']
    integrations: List['discord_typings.PartialIntegrationData']
    threads: List['discord_typings.ThreadChannelData']
    users: List['discord_typings.UserData']
    webhooks: List['discord_typings.WebhookData']


class PartialIntegrationData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    type: Literal['twitch', 'youtube', 'discord']
    account: 'discord_typings.IntegrationAccountData'
    application_id: 'discord_typings.Snowflake'


# https://discord.com/developers/docs/resources/audit-log#audit-log-entry-object-audit-log-entry-structure


class AuditLogEntryData(TypedDict):
    target_id: Optional[str]
    changes: NotRequired[List['discord_typings.AuditLogChangeData']]
    user_id: Optional['discord_typings.Snowflake']
    id: 'discord_typings.Snowflake'
    action_type: 'discord_typings.AuditLogEvents'
    options: NotRequired['discord_typings.OptionalAuditLogEntryData']
    reason: NotRequired[str]


# https://discord.com/developers/docs/resources/audit-log#audit-log-entry-object-audit-log-events


AuditLogEvents = Literal[
    1,
    10, 11, 12, 13, 14, 15,
    20, 21, 22, 23, 24, 25, 26, 27, 28,
    30, 31, 32,
    40, 41, 42,
    50, 51, 52,
    60, 61, 62,
    72, 73, 74, 75,
    80, 81, 82, 83, 84, 85,
    90, 91, 92,
    100, 101, 102,
    110, 111, 112,
    121,
    140, 141, 142, 143, 144, 145,
    150, 151
]


# https://discord.com/developers/docs/resources/audit-log#audit-log-entry-object-optional-audit-entry-info


class OptionalAuditLogEntryData(TypedDict):
    application_id: NotRequired['discord_typings.Snowflake']
    auto_moderation_rule_name: NotRequired[str]
    auto_moderation_trigger_type: NotRequired[str]  # AutoModerationTriggerTypes
    channel_id: NotRequired['discord_typings.Snowflake']
    count: NotRequired[str]
    delete_member_days: NotRequired[str]
    id: NotRequired['discord_typings.Snowflake']
    members_removed: NotRequired[str]
    message_id: NotRequired['discord_typings.Snowflake']
    role_name: NotRequired[str]
    type: NotRequired[Literal['0', '1']]
    integration_type: str


# https://discord.com/developers/docs/resources/audit-log#audit-log-change-object-audit-log-change-structure


class AuditLogChangeData(TypedDict):
    new_value: NotRequired[Any]
    old_value: NotRequired[Any]
    key: str
