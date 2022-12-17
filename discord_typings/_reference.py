from typing import Dict, List, Union

from typing_extensions import Literal, TypedDict, final

__all__ = [
    'Snowflake', 'HTTPErrorData', 'InnerHTTPErrorsData', 'NestedHTTPErrorsData',
    'HTTPErrorResponseData', 'Locales'
]


# Somewhat useless but good to distinguish the difference, perhaps in the
# future Python's typing system will have something similar to TypeScript's
# "Template Literal Types" which is able to describe a snowflake.
# Discord handles integers on endpoints but all snowflakes received by the API
# will be strings.
# https://discord.com/developers/docs/reference#snowflakes
Snowflake = Union[str, int]


# https://discord.com/developers/docs/reference#error-messages


@final
class HTTPErrorData(TypedDict):
    code: str
    message: str


@final
class InnerHTTPErrorsData(TypedDict):
    _errors: List[HTTPErrorData]


NestedHTTPErrorsData = Union[
    Dict[str, 'NestedHTTPErrorsData'],
    InnerHTTPErrorsData
]


@final
class HTTPErrorResponseData(TypedDict):
    code: int
    errors: NestedHTTPErrorsData
    message: str


# https://discord.com/developers/docs/reference#locales


Locales = Literal[
    'id',
    'da',
    'de',
    'en-GB',
    'en-US',
    'en-ES',
    'fr',
    'hr',
    'it',
    'lt',
    'hu',
    'nl',
    'no',
    'pl',
    'pt-BR',
    'ro',
    'fi',
    'sv-SE',
    'vi',
    'tr',
    'cs',
    'el',
    'bg',
    'ru',
    'uk',
    'hi',
    'th',
    'zh-CN',
    'ja',
    'zh-TW',
    'ko',
]
