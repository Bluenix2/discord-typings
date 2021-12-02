from typing import Optional

from typing_extensions import TypedDict

from ..shared import Snowflake
from .guild import GuildData
from .user import UserData

__all__ = ('GuildTemplateData',)

class GuildTemplateData(TypedDict):
    code: str
    name: str
    description: Optional[str]
    usage_count: int
    creator_id: Snowflake
    creator: UserData
    created_at: str
    updated_at: str
    source_guild_id: Snowflake
    serialized_source_guild: GuildData
    is_dirty: Optional[bool]
