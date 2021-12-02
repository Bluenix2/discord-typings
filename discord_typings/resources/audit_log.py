from __future__ import annotations

from typing import Any, List, Optional

from typing_extensions import Literal, NotRequired, TypedDict

from ..shared import Snowflake
from .channel import ThreadChannelData
from .guild import IntegrationAccountData
from .user import UserData
from .webhook import WebhookData


class AuditLogData(TypedDict):
    audit_log_entries: List[AuditLogEntryData]
    integrations: List[PartialIntegrationData]
    threads: List[ThreadChannelData]
    users: List[UserData]
    webhooks: List[WebhookData]


class PartialIntegrationData(TypedDict):
    id: Snowflake
    name: str
    type: Literal['twitch', 'youtube', 'discord']
    account: IntegrationAccountData


class AuditLogEntryData(TypedDict):
    target_id: Optional[str]
    changes: NotRequired[List[AuditLogChangeData]]
    user_id: Optional[Snowflake]
    id: Snowflake
    action_type: AuditLogEvents
    options: NotRequired[OptionalAuditLogEntryData]
    reason: NotRequired[str]


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


class OptionalAuditLogEntryData(TypedDict, total=False):
    channel_id: Snowflake
    count: str
    delete_member_days: str
    id: Snowflake
    members_removed: str
    message_id: str
    role_name: str
    type: str


class AuditLogChangeData(TypedDict):
    new_value: NotRequired[Any]
    old_value: NotRequired[Any]
    key: str
