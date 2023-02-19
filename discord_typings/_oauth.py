from __future__ import annotations

from typing import List

from typing_extensions import Literal, NotRequired, TypedDict, final

from ._resources import ApplicationData, UserData

__all__ = ('OAuth2Scopes', 'AccessTokenResponseData', 'AuthorizationInformationData')


# https://discord.com/developers/docs/topics/oauth2#shared-resources-oauth2-scopes


OAuth2Scopes = Literal[
    'activities.read',
    'activities.write',
    'applications.builds.read',
    'applications.build.upload',
    'applications.commands',
    'applications.commands.update',
    'applications.commands.permissions.update',
    'application.entitlements',
    'applications.store.update',
    'bot',
    'connections',
    'dm_channels.read',
    'email',
    'gdm.join',
    'guilds',
    'guilds.join',
    'guilds.members.read',
    'identify',
    'messages.read',
    'relationships.read',
    'role_connections.write',
    'rpc',
    'rpc.activities.write',
    'rpc.notifications.read',
    'rpc.voice.read',
    'rpc.voice.write',
    'voice',
    'webhook.incoming',
]


# https://discord.com/developers/docs/topics/oauth2#authorization-code-grant-access-token-response


@final
class AccessTokenResponseData(TypedDict):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str


# https://discord.com/developers/docs/topics/oauth2#get-current-authorization-information


@final
class AuthorizationInformationData(TypedDict):
    application: ApplicationData
    scopes: List[str]
    user: NotRequired[UserData]
    expires: str
