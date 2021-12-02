from __future__ import annotations

from typing import List, Optional

from typing_extensions import Literal, NotRequired, TypedDict

from .application import ApplicationData
from .channel import PartialChannelData
from .guild import GuildData, GuildMemberData
from .guild_scheduled_events import GuildScheduledEventData
from .user import UserData

__all__ = ('InviteData', 'InviteMetadata')


class InviteData(TypedDict):
    code: str
    guild: NotRequired[GuildData]
    channel: PartialChannelData
    inviter: NotRequired[UserData]
    target_type: Literal[1, 2]
    target_user: NotRequired[UserData]
    target_application: NotRequired[ApplicationData]
    approximate_presence_count: NotRequired[int]
    approximate_member_count: NotRequired[int]
    expires_at: NotRequired[Optional[str]]
    stage_instance: NotRequired[InviteStageInstanceData]
    guild_scheduled_event: NotRequired[GuildScheduledEventData]


class InviteMetadata(InviteData):
    uses: int
    max_uses: int
    max_age: int
    temporary: bool
    created_at: str


class InviteStageInstanceData(TypedDict):
    members: List[GuildMemberData]
    participant_count: int
    speaker_count: int
    topic: str
