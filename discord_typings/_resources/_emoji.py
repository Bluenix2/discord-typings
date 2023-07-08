from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

import discord_typings

__all__ = ('EmojiData',)


# https://discord.com/developers/docs/resources/emoji#emoji-object


class EmojiData(TypedDict):
    id: Optional['discord_typings.Snowflake']
    name: Optional[str]
    roles: NotRequired[List['discord_typings.Snowflake']]
    user: NotRequired['discord_typings.UserData']
    require_colons: NotRequired[bool]
    managed: NotRequired[bool]
    animated: NotRequired[bool]
    available: NotRequired[bool]
