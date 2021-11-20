from typing_extensions import Literal, TypedDict

from ..shared import Snowflake

__all__ = ('StageInstanceData',)


class StageInstanceData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    channel_id: Snowflake
    topic: str
    privacy_level: Literal[1, 2]
    discoverable_disabled: bool
