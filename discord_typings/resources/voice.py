from typing import TYPE_CHECKING, Optional

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    from ..shared import Snowflake
    from .guild import GuildMemberData

__all__ = ('VoiceStateData', 'VoiceRegionData')


# https://discord.com/developers/docs/resources/voice#voice-state-object-voice-state-structure


class VoiceStateData(TypedDict):
    guild_id: NotRequired[Snowflake]
    channel_id: Optional[Snowflake]
    user_id: Snowflake
    member: GuildMemberData
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    self_stream: NotRequired[bool]
    self_video: bool
    seppress: bool
    request_to_speak_timestamp: Optional[str]


# https://discord.com/developers/docs/resources/voice#voice-region-object-voice-region-structure


class VoiceRegionData(TypedDict):
    id: str
    name: str
    optimal: bool
    deprecated: bool
    custom: bool
