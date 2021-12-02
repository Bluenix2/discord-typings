from typing import List, Optional

from typing_extensions import Literal, NotRequired, TypedDict

from ..shared import Snowflake
from .user import UserData

__all__ = ('StickerItemData', 'StickerData', 'StickerPackData')


class StickerItemData(TypedDict):
    id: Snowflake
    name: str
    format_type: Literal[1, 2, 3]


class StickerData(StickerItemData):
    pack_id: NotRequired[Snowflake]
    description: Optional[str]
    tags: str
    type: Literal[1, 2]
    available: NotRequired[bool]
    guild_id: NotRequired[Snowflake]
    user: NotRequired[UserData]
    sort_value: NotRequired[int]


class StickerPackData(TypedDict):
    id: Snowflake
    stickers: List[StickerData]
    name: str
    sku_id: Snowflake
    cover_sticker_id: NotRequired[Snowflake]
    description: str
    banner_asset_id: Snowflake
