from typing import TYPE_CHECKING, List, Optional

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    from ..shared import Snowflake
    from .user import UserData

__all__ = ('EmojiData',)


# https://discord.com/developers/docs/resources/emoji#emoji-object-emoji-structure


class EmojiData(TypedDict):
    id: Optional[Snowflake]
    name: Optional[str]
    roles: NotRequired[List[Snowflake]]
    user: NotRequired[UserData]
    require_colons: NotRequired[bool]
    managed: NotRequired[bool]
    animated: NotRequired[bool]
    available: NotRequired[bool]
