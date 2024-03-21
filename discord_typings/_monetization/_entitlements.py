from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'EntitlementData',
    'EntitlementTypes',
)


# https://discord.com/developers/docs/monetization/entitlements#entitlement-object


class EntitlementData(TypedDict):
    id: 'discord_typings.Snowflake'
    sku_id: 'discord_typings.Snowflake'
    application_id: 'discord_typings.Snowflake'
    user_id: NotRequired['discord_typings.Snowflake']
    type: 'discord_typings.EntitlementTypes'
    deleted: bool
    starts_at: NotRequired[str]
    ends_at: NotRequired[str]
    guild_id: NotRequired['discord_typings.Snowflake']


# https://discord.com/developers/docs/monetization/entitlements#entitlement-object-entitlement-types


EntitlementTypes = Literal[8]
