from typing import Dict, List, Optional, Union

from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    'UserData',
    'UserPremiumTypes',
    'ConnectionData',
    'ConnectionTypes',
    'ConnectionVisibilityTypes',
    'ApplicationRoleConnectionData',
)

import discord_typings

# https://discord.com/developers/docs/resources/user#user-object-user-structure


class UserData(TypedDict):
    id: 'discord_typings.Snowflake'
    username: str
    discriminator: Union[str, Literal["0"]]
    global_name: Optional[str]
    avatar: Optional[str]
    bot: NotRequired[bool]
    system: NotRequired[bool]
    mfa_enabled: NotRequired[bool]
    banner: NotRequired[Optional[str]]
    accent_color: NotRequired[Optional[int]]
    locale: NotRequired['discord_typings.Locales']
    verified: NotRequired[bool]
    email: NotRequired[Optional[str]]
    flags: NotRequired[int]
    premium_type: NotRequired['discord_typings.UserPremiumTypes']
    public_flags: NotRequired[int]
    avatar_decoration: NotRequired[Optional[str]]


# https://discord.com/developers/docs/resources/user#user-object-premium-types


UserPremiumTypes = Literal[0, 1, 2, 3]


# https://discord.com/developers/docs/resources/user#connection-object


class ConnectionData(TypedDict):
    id: str
    name: str
    type: 'discord_typings.ConnectionTypes'
    revoked: NotRequired[bool]
    integrations: NotRequired[List['discord_typings.IntegrationData']]
    verified: bool
    friend_sync: bool
    show_activity: bool
    two_way_link: bool
    visibility: 'discord_typings.ConnectionVisibilityTypes'


# https://discord.com/developers/docs/resources/user#connection-object-services


ConnectionTypes = Literal[
    'battlenet',
    'ebay',
    'epicgames',
    'facebook',
    'github',
    'instagram',
    'leagueoflegends',
    'paypal',
    'playstation',
    'reddit',
    'riotgames',
    'spotify',
    'skype',
    'steam',
    'tiktok',
    'twitch',
    'twitter',
    'xbox',
    'youtube',
]


# https://discord.com/developers/docs/resources/user#connection-object-visibility-types


ConnectionVisibilityTypes = Literal[0, 1]


# https://discord.com/developers/docs/resources/user#application-role-connection-object


class ApplicationRoleConnectionData(TypedDict):
    platform_name: Optional[str]
    platform_username: Optional[str]
    metadata: Dict[str, str]
