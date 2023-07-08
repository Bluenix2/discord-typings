from typing import Dict, Generic, List, Optional, TypeVar, Union

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'ApplicationCommandData',
    'ApplicationCommandTypes',
    'SubcommandOptionData',
    'SubcommandGroupOptionData',
    'ApplicationCommandOptionData',
    'ApplicationCommandOptionTypes',
    'CommandOptionChoiceData',
    'GuildApplicationCommandPermissionData',
    'ApplicationCommandPermissionsData',
    'ApplicationCommandPermissionTypes',
    'ApplicationCommandPayload',
)


_T = TypeVar('_T')

# https://discord.com/developers/docs/interactions/application-commands#application-command-object


class _ChatInputCommandData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: NotRequired[Literal[1]]
    application_id: 'discord_typings.Snowflake'
    guild_id: NotRequired['discord_typings.Snowflake']
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    options: List['discord_typings.ApplicationCommandOptionData']
    default_member_permissions: Optional[str]
    dm_permission: NotRequired[bool]
    nsfw: NotRequired[bool]
    version: 'discord_typings.Snowflake'


class _ContextMenuCommandData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: NotRequired[Literal[2, 3]]
    application_id: 'discord_typings.Snowflake'
    guild_id: NotRequired['discord_typings.Snowflake']
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    default_member_permissions: Optional[str]
    dm_permission: NotRequired[bool]
    nsfw: NotRequired[bool]
    version: 'discord_typings.Snowflake'


ApplicationCommandData = Union[_ChatInputCommandData, _ContextMenuCommandData]


# https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-types


ApplicationCommandTypes = Literal[1, 2, 3]


# https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure

# The variations and overloads of options are huge, but we want to allow
# type narrowing. As a result, this becomes a very large union.

# While Discord only documents a "full" ApplicationCommandOptionData,
# due to the nature of subcommand options those are also exposed


class SubcommandOptionData(TypedDict):
    type: Literal[1]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    options: NotRequired[List['discord_typings.ApplicationCommandOptionData']]


class SubcommandGroupOptionData(TypedDict):
    type: Literal[2]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    options: List['discord_typings.SubcommandOptionData']


class _ChoicesStringOptionData(TypedDict):
    type: Literal[3]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]
    choices: NotRequired[List['discord_typings.CommandOptionChoiceData[str]']]


class _AutocompleteStringOptionData(TypedDict):
    type: Literal[3]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]
    autocomplete: NotRequired[bool]


class _MinMaxStringOptionData(TypedDict):
    type: Literal[3]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]
    min_length: NotRequired[int]
    max_length: NotRequired[int]


class _ChoicesIntegerCommandOptionData(TypedDict):
    type: Literal[4]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]
    choices: NotRequired[List['discord_typings.CommandOptionChoiceData[int]']]


class _MinMaxIntegerCommandOptionData(TypedDict):
    type: Literal[4]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]
    min_value: NotRequired[int]
    max_value: NotRequired[int]


class _AutocompleteIntegerOptionData(TypedDict):
    type: Literal[4]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]
    autocomplete: NotRequired[bool]


class _BooleanOptionData(TypedDict):
    type: Literal[5]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]


class _UserOptionData(TypedDict):
    type: Literal[6]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]


class _ChannelOptionData(TypedDict):
    type: Literal[7]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]
    channel_types: NotRequired[List['discord_typings.ChannelTypes']]


class _RoleOptionData(TypedDict):
    type: Literal[8]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]


class _MentionableOptionData(TypedDict):
    type: Literal[9]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]


class _ChoicesNumberCommandOptionData(TypedDict):
    type: Literal[10]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]
    choices: NotRequired[List['discord_typings.CommandOptionChoiceData[Union[int, float]]']]


class _MinMaxNumberCommandOptionData(TypedDict):
    type: Literal[10]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]
    min_value: NotRequired[Union[int, float]]
    max_value: NotRequired[Union[int, float]]


class _AutocompleteNumberOptionData(TypedDict):
    type: Literal[10]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]
    autocomplete: NotRequired[bool]


class _AttachmentOptionData(TypedDict):
    type: Literal[11]
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    required: NotRequired[bool]


ApplicationCommandOptionData = Union[
    SubcommandOptionData,
    SubcommandGroupOptionData,
    _ChoicesStringOptionData,
    _AutocompleteStringOptionData,
    _MinMaxStringOptionData,
    _ChoicesIntegerCommandOptionData,
    _MinMaxIntegerCommandOptionData,
    _AutocompleteIntegerOptionData,
    _BooleanOptionData,
    _UserOptionData,
    _ChannelOptionData,
    _RoleOptionData,
    _MentionableOptionData,
    _ChoicesNumberCommandOptionData,
    _MinMaxNumberCommandOptionData,
    _AutocompleteNumberOptionData,
    _AttachmentOptionData,
]


# https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-type


ApplicationCommandOptionTypes = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-choice-structure


class CommandOptionChoiceData(TypedDict, Generic[_T]):
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    value: _T


# https://discord.com/developers/docs/interactions/application-commands#application-command-permissions-object


class GuildApplicationCommandPermissionData(TypedDict):
    id: 'discord_typings.Snowflake'
    application_id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'
    permissions: List['discord_typings.ApplicationCommandPermissionsData']


# https://discord.com/developers/docs/interactions/application-commands#application-command-permissions-object-application-command-permissions-structure


class ApplicationCommandPermissionsData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: 'discord_typings.ApplicationCommandPermissionTypes'
    permission: bool


# https://discord.com/developers/docs/interactions/application-commands#application-command-permissions-object-application-command-permission-type


ApplicationCommandPermissionTypes = Literal[1, 2, 3]


# https://discord.com/developers/docs/interactions/application-commands#create-global-application-command-json-params


class ApplicationCommandPayload(TypedDict):
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: NotRequired[str]
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    options: NotRequired[List['discord_typings.ApplicationCommandOptionData']]
    default_member_permissions: NotRequired[Optional[str]]
    dm_permission: NotRequired[Optional[bool]]
    type: NotRequired['discord_typings.ApplicationCommandTypes']
    nsfw: NotRequired[bool]
