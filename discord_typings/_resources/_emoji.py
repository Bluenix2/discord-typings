from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from typing_extensions import NotRequired, TypedDict, final

if TYPE_CHECKING:
    from .._reference import Snowflake
    from ._user import UserData

__all__ = ('EmojiData',)


# https://discord.com/developers/docs/resources/emoji#emoji-object-emoji-structure


@final
class EmojiData(TypedDict):
    id: Optional[Snowflake]
    name: Optional[str]
    roles: NotRequired[List[Snowflake]]
    user: NotRequired[UserData]
    require_colons: NotRequired[bool]
    managed: NotRequired[bool]
    animated: NotRequired[bool]
    available: NotRequired[bool]
