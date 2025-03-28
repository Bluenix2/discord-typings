from typing import Union

from typing_extensions import TypedDict

import discord_typings

__all__ = (
    'APISnowflake',
    'APIError',
    'APIInnerErrors',
    'APIErrorDetails',
    'APIErrorResponse',
)


# Somewhat useless but good to distinguish the difference, perhaps in the
# future Python's typing system will have something similar to TypeScript's
# "Template Literal Types" which is able to describe a snowflake.
# Discord handles integers on endpoints but all snowflakes received by the API
# will be strings.
# https://discord.com/developers/docs/reference#snowflakes
APISnowflake = Union[str, int]


# https://discord.com/developers/docs/reference#error-messages


class APIError(TypedDict):
    code: int
    message: str


class APIInnerErrors(TypedDict):
    _errors: list['discord_typings.APIError']


APIErrorDetails = Union[
    dict[str, 'discord_typings.APIErrorDetails'],
    APIInnerErrors,
]


class APIErrorResponse(APIError):
    errors: APIErrorDetails
