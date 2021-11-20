from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..shared import Snowflake
from .user import UserData

__all__ = ('EmojiData',)


class EmojiData(TypedDict):
    id: Optional[Snowflake]
    name: Optional[str]
    roles: NotRequired[List[Snowflake]]
    user: NotRequired[UserData]
    require_colons: NotRequired[bool]
    managed: NotRequired[bool]
    animated: NotRequired[bool]
    available: NotRequired[bool]
