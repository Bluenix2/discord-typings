from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from typing_extensions import Literal, TypedDict, final

if TYPE_CHECKING:
    from .._reference import Snowflake

__all__ = ('StageInstanceData', 'StageInstancePrivacyLevels')


# https://discord.com/developers/docs/resources/stage-instance#stage-instance-object-stage-instance-structure


@final
class StageInstanceData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    channel_id: Snowflake
    topic: str
    privacy_level: StageInstancePrivacyLevels
    discoverable_disabled: bool
    guild_scheduled_event_id: Optional[Snowflake]


# https://discord.com/developers/docs/resources/stage-instance#stage-instance-object-privacy-level


StageInstancePrivacyLevels = Literal[1, 2]
