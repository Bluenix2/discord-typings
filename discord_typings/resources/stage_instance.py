from typing import TYPE_CHECKING

from typing_extensions import Literal, TypedDict

if TYPE_CHECKING:
    from ..shared import Snowflake

__all__ = ('StageInstanceData',)


# https://discord.com/developers/docs/resources/stage-instance#stage-instance-object-stage-instance-structure


class StageInstanceData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    channel_id: Snowflake
    topic: str
    privacy_level: Literal[1, 2]
    discoverable_disabled: bool
