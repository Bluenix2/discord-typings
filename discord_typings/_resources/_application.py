from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from typing_extensions import NotRequired, TypedDict, final

if TYPE_CHECKING:
    from .._reference import Snowflake
    from ._user import UserData

__all__ = ('ApplicationData', 'TeamData', 'TeamMemberData', 'InstallParams')


# https://discord.com/developers/docs/resources/application#application-object-application-structure


@final
class ApplicationData(TypedDict):
    id: Snowflake
    name: str
    icon: Optional[str]
    description: str
    rpc_origins: NotRequired[List[str]]
    bot_public: bool
    bot_require_code_grant: bool
    terms_of_service_url: NotRequired[str]
    privacy_policy_url: NotRequired[str]
    owner: NotRequired[UserData]
    verify_key: str
    team: Optional[TeamData]
    guild_id: NotRequired[Snowflake]
    primary_sku_id: NotRequired[Snowflake]
    slug: NotRequired[str]
    cover_image: NotRequired[str]
    flags: NotRequired[int]
    tags: NotRequired[List[str]]
    install_params: NotRequired[InstallParams]
    custom_install_url: NotRequired[str]
    role_connections_verification_url: NotRequired[str]


# https://discord.com/developers/docs/resources/application#install-params-object-install-params-structure


@final
class InstallParams(TypedDict):
    scopes: List[str]
    permissions: str


# https://discord.com/developers/docs/topics/teams#data-models-team-object


@final
class TeamData(TypedDict):
    icon: Optional[str]
    id: Snowflake
    members: List[TeamMemberData]
    name: str
    owner_user_id: Snowflake


# https://discord.com/developers/docs/topics/teams#data-models-team-member-object


@final
class TeamMemberData(TypedDict):
    membership_state: int
    permissions: List[str]
    team_id: Snowflake
    user: UserData
