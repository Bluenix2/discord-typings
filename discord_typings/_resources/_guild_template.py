from typing import Optional

from typing_extensions import TypedDict

import discord_typings

__all__ = ('GuildTemplateData',)


# https://discord.com/developers/docs/resources/guild-template#guild-template-object


class GuildTemplateData(TypedDict):
    code: str
    name: str
    description: Optional[str]
    usage_count: int
    creator_id: 'discord_typings.Snowflake'
    creator: 'discord_typings.UserData'
    created_at: str
    updated_at: str
    source_guild_id: 'discord_typings.Snowflake'
    serialized_source_guild: 'discord_typings.GuildData'
    is_dirty: Optional[bool]
