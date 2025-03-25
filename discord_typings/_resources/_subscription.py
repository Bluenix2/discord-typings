from typing import List, Optional

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'SubscriptionData',
    'SubscriptionStatuses',
)


# https://discord.com/developers/docs/resources/subscription#subscription-object


class SubscriptionData(TypedDict):
    id: 'discord_typings.Snowflake'
    user_id: 'discord_typings.Snowflake'
    sku_ids: List['discord_typings.Snowflake']
    entitlements_ids: List['discord_typings.Snowflake']
    renewal_sku_ids: Optional[List['discord_typings.Snowflake']]
    current_period_start: str
    current_period_end: str
    status: 'discord_typings.SubscriptionStatuses'
    canceled_at: Optional[str]
    country: NotRequired[str]


# https://discord.com/developers/docs/resources/subscription#subscription-statuses


SubscriptionStatuses = Literal[0, 1, 2]
