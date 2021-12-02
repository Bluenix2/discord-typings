from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..shared import Snowflake
from .user import UserData

__all__ = ('ApplicationData', 'TeamData', 'TeamMemberData')


class ApplicationData(TypedDict):
    id: Snowflake
    name: str
    icon: Optional[str]
    description: str
    rpc_origins: List[str]
    bot_public: bool
    bot_require_code_grant: bool
    terms_of_service_url: NotRequired[str]
    privacy_policy_url: NotRequired[str]
    owner: NotRequired[UserData]
    summary: str
    verify_key: str
    team: Optional[TeamData]
    guild_id: NotRequired[Snowflake]
    primary_sku_id: NotRequired[Snowflake]
    slug: NotRequired[str]
    cover_image: NotRequired[str]
    flags: NotRequired[int]


class TeamData(TypedDict):
    icon: Optional[str]
    id: Snowflake
    members: List[TeamMemberData]
    name: str
    owner_user_id: Snowflake


class TeamMemberData(TypedDict):
    membership_state: int
    permissions: List[str]
    team_id: Snowflake
    user: UserData
