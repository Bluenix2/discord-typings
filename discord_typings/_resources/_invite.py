from typing import List, Optional

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'InviteData',
    'InviteTargetTypes',
    'InviteMetadata',
    'InviteStageInstanceData',
)


# https://discord.com/developers/docs/resources/invite#invite-object-invite-structure


class InviteData(TypedDict):
    code: str
    guild: NotRequired['discord_typings.PartialGuildData']
    channel: Optional['discord_typings.PartialChannelData']
    inviter: NotRequired['discord_typings.UserData']
    target_type: NotRequired['discord_typings.InviteTargetTypes']
    target_user: NotRequired['discord_typings.UserData']
    target_application: NotRequired['discord_typings.ApplicationData']
    approximate_presence_count: NotRequired[int]
    approximate_member_count: NotRequired[int]
    expires_at: NotRequired[Optional[str]]
    stage_instance: NotRequired['discord_typings.InviteStageInstanceData']
    guild_scheduled_event: NotRequired['discord_typings.GuildScheduledEventData']


# https://discord.com/developers/docs/resources/invite#invite-object-invite-target-types


InviteTargetTypes = Literal[1, 2]


# https://discord.com/developers/docs/resources/invite#invite-metadata-object-invite-metadata-structure


class InviteMetadata(InviteData):
    uses: int
    max_uses: int
    max_age: int
    temporary: bool
    created_at: str


# https://discord.com/developers/docs/resources/invite#invite-stage-instance-object-invite-stage-instance-structure


class InviteStageInstanceData(TypedDict):
    members: List['discord_typings.GuildMemberData']
    participant_count: int
    speaker_count: int
    topic: str
