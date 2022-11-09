from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from ._application import ApplicationData
    from ._channel import PartialChannelData
    from ._guild import GuildMemberData, PartialGuildData
    from ._guild_scheduled_events import GuildScheduledEventData
    from ._user import UserData

__all__ = ('InviteData', 'InviteTargetTypes', 'InviteMetadata', 'InviteStageInstanceData')


# https://discord.com/developers/docs/resources/invite#invite-object-invite-structure


class _InviteBase(TypedDict):
    code: str
    guild: NotRequired[PartialGuildData]
    channel: Optional[PartialChannelData]
    inviter: NotRequired[UserData]
    target_type: NotRequired[InviteTargetTypes]
    target_user: NotRequired[UserData]
    target_application: NotRequired[ApplicationData]
    approximate_presence_count: NotRequired[int]
    approximate_member_count: NotRequired[int]
    expires_at: NotRequired[Optional[str]]
    stage_instance: NotRequired[InviteStageInstanceData]
    guild_scheduled_event: NotRequired[GuildScheduledEventData]


@final
class InviteData(_InviteBase):
    pass


# https://discord.com/developers/docs/resources/invite#invite-object-invite-target-types


InviteTargetTypes = Literal[1, 2]


# https://discord.com/developers/docs/resources/invite#invite-metadata-object-invite-metadata-structure


@final
class InviteMetadata(_InviteBase):
    uses: int
    max_uses: int
    max_age: int
    temporary: bool
    created_at: str


# https://discord.com/developers/docs/resources/invite#invite-stage-instance-object-invite-stage-instance-structure


@final
class InviteStageInstanceData(TypedDict):
    members: List[GuildMemberData]
    participant_count: int
    speaker_count: int
    topic: str
