from typing import Optional

from typing_extensions import NotRequired, TypedDict

import discord_typings

__all__ = (
    'VoiceStateData',
    'VoiceRegionData',
)


# https://discord.com/developers/docs/resources/voice#voice-state-object-voice-state-structure


class VoiceStateData(TypedDict):
    guild_id: NotRequired['discord_typings.Snowflake']
    channel_id: Optional['discord_typings.Snowflake']
    user_id: 'discord_typings.Snowflake'
    member: NotRequired['discord_typings.GuildMemberData']
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    self_stream: NotRequired[bool]
    self_video: bool
    suppress: bool
    request_to_speak_timestamp: Optional[str]


# https://discord.com/developers/docs/resources/voice#voice-region-object-voice-region-structure


class VoiceRegionData(TypedDict):
    id: str
    name: str
    optimal: bool
    deprecated: bool
    custom: bool
