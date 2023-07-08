from typing import List, Optional

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'StickerItemData',
    'StickerTypes',
    'StickerFormatTypes',
    'StickerData',
    'StickerPackData',
)


# https://discord.com/developers/docs/resources/sticker#sticker-item-object


# Because of inheritance, this class comes first even though that is not the
# order in the documentation.
class StickerItemData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    format_type: 'discord_typings.StickerFormatTypes'


# https://discord.com/developers/docs/resources/sticker#sticker-object-sticker-types


StickerTypes = Literal[1, 2]


# https://discord.com/developers/docs/resources/sticker#sticker-object-sticker-format-types


StickerFormatTypes = Literal[1, 2, 3, 4]


# https://discord.com/developers/docs/resources/sticker#sticker-object-sticker-structure


class StickerData(StickerItemData):
    pack_id: NotRequired['discord_typings.Snowflake']
    description: Optional[str]
    tags: str
    type: StickerTypes
    available: NotRequired[bool]
    guild_id: NotRequired['discord_typings.Snowflake']
    user: NotRequired['discord_typings.UserData']
    sort_value: NotRequired[int]


# https://discord.com/developers/docs/resources/sticker#sticker-pack-object


class StickerPackData(TypedDict):
    id: 'discord_typings.Snowflake'
    stickers: List['discord_typings.StickerData']
    name: str
    sku_id: 'discord_typings.Snowflake'
    cover_sticker_id: NotRequired['discord_typings.Snowflake']
    description: str
    banner_asset_id: NotRequired['discord_typings.Snowflake']
