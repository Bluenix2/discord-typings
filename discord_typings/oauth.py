from __future__ import annotations
from typing import List

from typing_extensions import NotRequired, TypedDict

from .resources.application import ApplicationData
from .resources.user import UserData

__all__ = ('AuthorizationInformation',)

# https://discord.com/developers/docs/topics/oauth2#get-current-authorization-information

class AuthorizationInformation(TypedDict):
    application: ApplicationData
    scopes: List[str]
    user: NotRequired[UserData]
    expires: str
