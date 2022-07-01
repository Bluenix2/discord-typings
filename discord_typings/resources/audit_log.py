from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from ..reference import Snowflake
    from .channel import ThreadChannelData
    from .guild import IntegrationAccountData
    from .user import UserData
    from .webhook import WebhookData

__all__ = (
    'AuditLogData', 'AuditLogEntryData', 'OptionalAuditLogEntryData', 'AuditLogChangeData'
)


# https://discord.com/developers/docs/resources/audit-log#audit-log-object-audit-log-structure


@final
class AuditLogData(TypedDict):
    audit_log_entries: List[AuditLogEntryData]
    integrations: List[PartialIntegrationData]
    threads: List[ThreadChannelData]
    users: List[UserData]
    webhooks: List[WebhookData]


@final
class PartialIntegrationData(TypedDict):
    id: Snowflake
    name: str
    type: Literal['twitch', 'youtube', 'discord']
    account: IntegrationAccountData


# https://discord.com/developers/docs/resources/audit-log#audit-log-entry-object-audit-log-entry-structure


@final
class AuditLogEntryData(TypedDict):
    target_id: Optional[str]
    changes: NotRequired[List[AuditLogChangeData]]
    user_id: Optional[Snowflake]
    id: Snowflake
    action_type: AuditLogEvents
    options: NotRequired[OptionalAuditLogEntryData]
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
    110, 111, 112
]


# https://discord.com/developers/docs/resources/audit-log#audit-log-entry-object-optional-audit-entry-info


@final
class OptionalAuditLogEntryData(TypedDict):
    channel_id: NotRequired[Snowflake]
    count: NotRequired[str]
    delete_member_days: NotRequired[str]
    id: NotRequired[Snowflake]
    members_removed: NotRequired[str]
    message_id: NotRequired[str]
    role_name: NotRequired[str]
    type: NotRequired[str]


# https://discord.com/developers/docs/resources/audit-log#audit-log-change-object-audit-log-change-structure


@final
class AuditLogChangeData(TypedDict):
    new_value: NotRequired[Any]
    old_value: NotRequired[Any]
    key: str
