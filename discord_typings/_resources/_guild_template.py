from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from typing_extensions import TypedDict, final

if TYPE_CHECKING:
    from .._reference import Snowflake
    from ._guild import GuildData
    from ._user import UserData

__all__ = ('GuildTemplateData',)


# https://discord.com/developers/docs/resources/invite#invite-stage-instance-object-invite-stage-instance-structure


@final
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
