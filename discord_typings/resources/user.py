from __future__ import annotations

from typing import Optional

from typing_extensions import Literal, NotRequired, TypedDict, final

__all__ = ('UserData', 'UserPremiumTypes')


# https://discord.com/developers/docs/resources/user#user-object-user-structure


class UserBase(TypedDict):
    id: str
    username: str
    discriminator: str
    avatar: Optional[str]
    bot: NotRequired[bool]
    system: NotRequired[bool]
    mfa_enabled: NotRequired[bool]
    banner: NotRequired[Optional[str]]
    accent_color: NotRequired[Optional[int]]
    locale: NotRequired[str]
    verified: NotRequired[bool]
    email: NotRequired[Optional[bool]]
    flags: NotRequired[int]
    premium_type: NotRequired[UserPremiumTypes]
    public_flags: NotRequired[int]


@final
class UserData(UserBase):
    pass


# https://discord.com/developers/docs/resources/user#user-object-premium-types


UserPremiumTypes = Literal[0, 1, 2]
