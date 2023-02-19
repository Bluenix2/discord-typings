from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from .._reference import Snowflake
    from ._user import UserData

__all__ = [
    'StickerItemData', 'StickerTypes', 'StickerFormatTypes', 'StickerData',
    'StickerPackData',
]


# https://discord.com/developers/docs/resources/sticker#sticker-item-object-sticker-item-structure


# Because of inheritance, this class comes first even though that is not the
# order in the documentation.
class _StickerItemBase(TypedDict):
    id: Snowflake
    name: str
    format_type: StickerFormatTypes


@final
class StickerItemData(_StickerItemBase):
    pass


# https://discord.com/developers/docs/resources/sticker#sticker-object-sticker-types


StickerTypes = Literal[1, 2]


# https://discord.com/developers/docs/resources/sticker#sticker-object-sticker-format-types


StickerFormatTypes = Literal[1, 2, 3, 4]


# https://discord.com/developers/docs/resources/sticker#sticker-object-sticker-structure


@final
class StickerData(_StickerItemBase):
    pack_id: NotRequired[Snowflake]
    description: Optional[str]
    tags: str
    type: StickerTypes
    available: NotRequired[bool]
    guild_id: NotRequired[Snowflake]
    user: NotRequired[UserData]
    sort_value: NotRequired[int]


# https://discord.com/developers/docs/resources/sticker#sticker-pack-object-sticker-pack-structure


@final
class StickerPackData(TypedDict):
    id: Snowflake
    stickers: List[StickerData]
    name: str
    sku_id: Snowflake
    cover_sticker_id: NotRequired[Snowflake]
    description: str
    banner_asset_id: NotRequired[Snowflake]
