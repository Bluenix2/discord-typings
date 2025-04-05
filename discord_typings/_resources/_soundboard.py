from typing import Optional

from typing_extensions import NotRequired, TypedDict

import discord_typings

__all__ = (
    'SoundboardSoundData',
)


# https://discord.com/developers/docs/resources/soundboard#soundboard-sound-object


class SoundboardSoundData(TypedDict):
    name: str
    sound_id: 'discord_typings.Snowflake'
    volume: float
    emoji_id: Optional['discord_typings.Snowflake']
    emoji_name: Optional[str]
    guild_id: NotRequired['discord_typings.Snowflake']
    available: bool
    user: NotRequired['discord_typings.UserData']
