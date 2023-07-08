from typing import Optional

from typing_extensions import Literal, TypedDict

import discord_typings

__all__ = (
    'StageInstanceData',
    'StageInstancePrivacyLevels',
)


# https://discord.com/developers/docs/resources/stage-instance#stage-instance-object-stage-instance-structure


class StageInstanceData(TypedDict):
    id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'
    channel_id: 'discord_typings.Snowflake'
    topic: str
    privacy_level: 'discord_typings.StageInstancePrivacyLevels'
    discoverable_disabled: bool
    guild_scheduled_event_id: Optional['discord_typings.Snowflake']


# https://discord.com/developers/docs/resources/stage-instance#stage-instance-object-privacy-level


StageInstancePrivacyLevels = Literal[1, 2]
