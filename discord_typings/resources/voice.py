from typing import Optional

from typing_extensions import NotRequired, TypedDict

from ..shared import Snowflake
from .guild import GuildMemberData

__all__ = ('VoiceStateData', 'VoiceRegionData')


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


class VoiceRegionData(TypedDict):
    id: str
    name: str
    optimal: bool
    deprecated: bool
    custom: bool
