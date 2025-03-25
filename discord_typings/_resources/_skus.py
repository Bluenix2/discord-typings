from typing_extensions import Literal, TypedDict

import discord_typings

__all__ = (
    'SKUData',
    'SKUTypes',
)


# https://discord.com/developers/docs/monetization/skus#sku-object


class SKUData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: 'discord_typings.SKUTypes'
    application_id: 'discord_typings.Snowflake'
    name: str
    slug: str
    flags: int


# https://discord.com/developers/docs/monetization/skus#sku-object-sku-types


SKUTypes = Literal[
    2,
    3,
    5,
    6,
]
