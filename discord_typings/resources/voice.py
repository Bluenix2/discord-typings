from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from typing_extensions import NotRequired, TypedDict, final

if TYPE_CHECKING:
    from ..shared import Snowflake
    from .guild import GuildMemberData

__all__ = ('VoiceStateData', 'VoiceRegionData', 'VoiceServerData')


# https://discord.com/developers/docs/resources/voice#voice-state-object-voice-state-structure


@final
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


@final
class VoiceRegionData(TypedDict):
    id: str
    name: str
    optimal: bool
    deprecated: bool
    custom: bool
        
        
# https://discord.com/developers/docs/topics/gateway#voice-server-update-voice-server-update-event-fields


@final
class VoiceServerData(TypedDict):
    token: str
    guild_id: Snowflake
    endpoint: Optional[str]
