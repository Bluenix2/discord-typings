from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional, Union

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from .._reference import Locales, Snowflake
    from .._resources import ChannelTypes

__all__ = (
    'ApplicationCommandData', 'ApplicationCommandTypes', 'SubcommandOptionData',
    'SubcommandGroupOptionData', 'AutocompleteOptionData', 'ApplicationCommandOptionData',
    'GuildApplicationCommandPermissionData', 'ApplicationCommandPermissionsData',
    'ApplicationCommandPayload', 'EditApplicationCommandPermissionsData'
)


# https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-structure


@final
class ChatInputCommandData(TypedDict):
    id: Snowflake
    type: NotRequired[Literal[1]]
    application_id: Snowflake
    guild_id: NotRequired[Snowflake]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    options: List[ApplicationCommandOptionData]
    default_member_permissions: NotRequired[Optional[str]]
    dm_permission: NotRequired[bool]
    nsfw: NotRequired[bool]
    version: Snowflake


@final
class ContextMenuCommandData(TypedDict):
    id: Snowflake
    type: NotRequired[Literal[2, 3]]
    application_id: Snowflake
    guild_id: NotRequired[Snowflake]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    default_member_permissions: NotRequired[Optional[str]]
    dm_permission: NotRequired[bool]
    nsfw: NotRequired[bool]
    version: Snowflake


ApplicationCommandData = Union[ChatInputCommandData, ContextMenuCommandData]


# https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-types


ApplicationCommandTypes = Literal[1, 2, 3]


# https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
# The variations and overloads of options are huge, but we want to provide
# extremely accurate typing - this is gonna be a huge Union with a lot of
# TypedDict subclasses...


@final
class SubcommandOptionData(TypedDict):
    type: Literal[1]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    options: NotRequired[List[ApplicationCommandOptionData]]


@final
class SubcommandGroupOptionData(TypedDict):
    type: Literal[2]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    options: List[SubcommandOptionData]


@final
class ChoicesStringOptionData(TypedDict):
    type: Literal[3]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]
    choices: NotRequired[List[StrCommandOptionChoiceData]]


@final
class AutocompleteStringOptionData(TypedDict):
    type: Literal[3]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]
    autocomplete: NotRequired[bool]


@final
class MinMaxStringOptionData(TypedDict):
    type: Literal[3]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]
    min_length: NotRequired[int]
    max_length: NotRequired[int]


@final
class ChoicesIntegerCommandOptionData(TypedDict):
    type: Literal[4]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]
    choices: NotRequired[List[IntCommandOptionChoiceData]]


@final
class MinMaxIntegerCommandOptionData(TypedDict):
    type: Literal[4]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]
    min_value: NotRequired[int]
    max_value: NotRequired[int]


@final
class AutocompleteIntegerOptionData(TypedDict):
    type: Literal[4]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]
    autocomplete: NotRequired[bool]


@final
class BooleanOptionData(TypedDict):
    type: Literal[5]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]


@final
class UserOptionData(TypedDict):
    type: Literal[6]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]


@final
class ChannelOptionData(TypedDict):
    type: Literal[7]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]
    channel_types: NotRequired[List[ChannelTypes]]


@final
class RoleOptionData(TypedDict):
    type: Literal[8]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]


@final
class MentionableOptionData(TypedDict):
    type: Literal[9]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]


@final
class ChoicesNumberCommandOptionData(TypedDict):
    type: Literal[10]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]
    choices: NotRequired[List[NumberCommandOptionChoiceData]]


@final
class MinMaxNumberCommandOptionData(TypedDict):
    type: Literal[10]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]
    min_value: NotRequired[Union[int, float]]
    max_value: NotRequired[Union[int, float]]


@final
class AutocompleteNumberOptionData(TypedDict):
    type: Literal[10]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]
    autocomplete: NotRequired[bool]


@final
class AttachmentOptionData(TypedDict):
    type: Literal[11]
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]
    required: NotRequired[bool]


AutocompleteOptionData = Union[
    AutocompleteStringOptionData, AutocompleteIntegerOptionData,
    AutocompleteNumberOptionData
]


ApplicationCommandOptionData = Union[
    ChoicesStringOptionData, ChoicesIntegerCommandOptionData,
    MinMaxIntegerCommandOptionData, MinMaxStringOptionData, BooleanOptionData,
    UserOptionData, ChannelOptionData, RoleOptionData, MentionableOptionData,
    ChoicesNumberCommandOptionData, MinMaxNumberCommandOptionData,
    AutocompleteOptionData, SubcommandOptionData, AttachmentOptionData,
]


# https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-type


ApplicationCommandOptionTypes = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-choice-structure


@final
class StrCommandOptionChoiceData(TypedDict):
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    value: str


@final
class IntCommandOptionChoiceData(TypedDict):
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    value: int


@final
class NumberCommandOptionChoiceData(TypedDict):
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    value: Union[int, float]


# https://discord.com/developers/docs/interactions/application-commands#application-command-permissions-object-guild-application-command-permissions-structure


@final
class GuildApplicationCommandPermissionData(TypedDict):
    id: Snowflake
    application_id: Snowflake
    guild_id: Snowflake
    permissions: List[ApplicationCommandPermissionsData]


# https://discord.com/developers/docs/interactions/application-commands#application-command-permissions-object-application-command-permissions-structure


@final
class ApplicationCommandPermissionsData(TypedDict):
    id: Snowflake
    type: ApplicationCommandPermissionTypes
    permission: bool


# https://discord.com/developers/docs/interactions/application-commands#application-command-permissions-object-application-command-permission-type


ApplicationCommandPermissionTypes = Literal[1, 2, 3]


# https://discord.com/developers/docs/interactions/application-commands#create-global-application-command-json-params


@final
class ApplicationCommandPayload(TypedDict):
    name: str
    description: NotRequired[str]
    options: NotRequired[List[ApplicationCommandOptionData]]
    default_member_permissions: NotRequired[Optional[str]]
    dm_permission: NotRequired[bool]
    type: NotRequired[Literal[1, 2, 3]]
    nsfw: NotRequired[bool]


# https://discord.com/developers/docs/interactions/application-commands#batch-edit-application-command-permissions-example


@final
class EditApplicationCommandPermissionsData(TypedDict):
    id: Snowflake
    permissions: ApplicationCommandPermissionsData
