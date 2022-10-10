from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from typing_extensions import Literal, NotRequired, TypedDict, final

__all__ = ("UserData", "UserPremiumTypes", "ConnectionData", "ConnectionTypes")

if TYPE_CHECKING:
    from ..interactions import Locales
    from ..reference import Snowflake
    from ..guild import IntegrationData


# https://discord.com/developers/docs/resources/user#user-object-user-structure


class UserBase(TypedDict):
    id: Snowflake
    username: str
    discriminator: str
    avatar: Optional[str]
    bot: NotRequired[bool]
    system: NotRequired[bool]
    mfa_enabled: NotRequired[bool]
    banner: NotRequired[Optional[str]]
    accent_color: NotRequired[Optional[int]]
    locale: NotRequired[Locales]
    verified: NotRequired[bool]
    email: NotRequired[Optional[str]]
    flags: NotRequired[int]
    premium_type: NotRequired[UserPremiumTypes]
    public_flags: NotRequired[int]


@final
class UserData(UserBase):
    pass


# https://discord.com/developers/docs/resources/user#user-object-premium-types


UserPremiumTypes = Literal[0, 1, 2]


# https://discord.com/developers/docs/resources/user#connection-object


ConnectionTypes = Literal[
    "battlenet",
    "ebay",
    "epicgames",
    "facebook",
    "github",
    "leagueoflegends",
    "paypal",
    "playstation",
    "reddit",
    "riotgames",
    "spotify",
    "skype",
    "steam",
    "twitch",
    "twitter",
    "xbox",
    "youtube",
]


@final
class ConnectionData(TypedDict):
    id: str
    name: str
    type: ConnectionTypes
    revoked: NotRequired[bool]
    integrations: NotRequired[List[IntegrationData]]
    verified: bool
    friend_sync: bool
    show_activity: bool
    two_way_link: bool
    visibility: Literal[0, 1]
