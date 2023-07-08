from typing import Optional

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'WebhookData',
    'WebhookTypes',
)


# https://discord.com/developers/docs/resources/webhook#webhook-object-webhook-structure


class WebhookData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: 'discord_typings.WebhookTypes'
    guild_id: NotRequired[Optional['discord_typings.Snowflake']]
    channel_id: Optional['discord_typings.Snowflake']
    user: NotRequired['discord_typings.UserData']
    name: Optional[str]
    avatar: Optional[str]
    token: NotRequired[str]
    application_id: Optional['discord_typings.Snowflake']
    source_guild: NotRequired['discord_typings.GuildData']
    source_channel: NotRequired['discord_typings.PartialChannelData']
    url: NotRequired[str]


# https://discord.com/developers/docs/resources/webhook#webhook-object-webhook-types


WebhookTypes = Literal[1, 2, 3]
