from __future__ import annotations

from typing import Dict, Generic, List, TypeVar, Union

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'PingInteractionData',
    'ApplicationCommandInteractionData',
    'ComponentInteractionData',
    'AutocompleteInteractionData',
    'ModalInteractionData',
    'InteractionData',
    'InteractionType',
    'ApplicationCommandInteractionDataData',
    'ComponentInteractionDataData',
    'ModalSubmitInteractionDataData',
    'InteractionDataData',
    'ResolvedInteractionDataData',
    'ApplicationCommandOptionInteractionData',
    'MessageInteractionData',
    'InteractionResponseData',
    'InteractionCallbackTypes',
    'InteractionMessageCallbackData',
    'InteractionAutocompleteCallbackData',
    'InteractionModalCallbackData',
    'InteractionCallbackData',
)


_T = TypeVar('_T')


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object


class PingInteractionData(TypedDict):
    id: 'discord_typings.Snowflake'
    application_id: 'discord_typings.Snowflake'
    type: Literal[1]
    user: 'discord_typings.UserData'
    version: int


class _GuildInteractionData(TypedDict):
    id: 'discord_typings.Snowflake'
    application_id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'
    channel: 'discord_typings.PartialChannelData'
    channel_id: 'discord_typings.Snowflake'
    member: 'discord_typings.GuildMemberData'
    token: str
    version: int
    app_permissions: str
    locale: 'discord_typings.Locales'
    guild_locale: 'discord_typings.Locales'


class _ApplicationCommandGuildInteractionData(_GuildInteractionData):
    type: Literal[2]
    data: 'discord_typings.ApplicationCommandInteractionDataData'


class _ComponentGuildInteractionData(_GuildInteractionData):
    type: Literal[3]
    data: ComponentInteractionDataData
    message: 'discord_typings.MessageData'


class _AutocompleteGuildInteractionData(_GuildInteractionData):
    type: Literal[4]
    data: 'discord_typings.ApplicationCommandInteractionDataData'


class _ModalGuildInteractionData(_GuildInteractionData):
    type: Literal[5]
    data: 'discord_typings.ModalSubmitInteractionDataData'


class _ChannelInteractionData(TypedDict):
    id: 'discord_typings.Snowflake'
    application_id: 'discord_typings.Snowflake'
    channel: 'discord_typings.PartialChannelData'
    channel_id: 'discord_typings.Snowflake'
    user: 'discord_typings.UserData'
    token: str
    version: int
    locale: 'discord_typings.Locales'


class _ApplicationCommandChannelInteractionData(_ChannelInteractionData):
    type: Literal[2]
    data: 'discord_typings.ApplicationCommandInteractionDataData'


class _ComponentChannelInteractionData(_ChannelInteractionData):
    type: Literal[3]
    data: 'discord_typings.ComponentInteractionDataData'
    message: 'discord_typings.MessageData'


class _AutocompleteChannelInteractionData(_ChannelInteractionData):
    type: Literal[4]
    data: 'discord_typings.ApplicationCommandInteractionDataData'


class _ModalChannelInteractionData(_ChannelInteractionData):
    type: Literal[5]
    data: 'discord_typings.ModalSubmitInteractionDataData'


ApplicationCommandInteractionData = Union[
    _ApplicationCommandGuildInteractionData, _ApplicationCommandChannelInteractionData,
]


ComponentInteractionData = Union[
    _ComponentGuildInteractionData, _ComponentChannelInteractionData
]


AutocompleteInteractionData = Union[
    _AutocompleteGuildInteractionData, _AutocompleteChannelInteractionData
]


ModalInteractionData = Union[
    _ModalGuildInteractionData, _ModalChannelInteractionData
]


InteractionData = Union[
    ApplicationCommandInteractionData, ComponentInteractionData, AutocompleteInteractionData,
    ModalInteractionData,
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-interaction-type


InteractionType = Literal[1, 2, 3, 4, 5]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-application-command-data-structure


class _ChatInputCommandInteractionDataData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    type: Literal[1]
    resolved: NotRequired[ResolvedInteractionDataData]
    options: NotRequired[List[ApplicationCommandOptionInteractionData]]
    guild_id: NotRequired['discord_typings.Snowflake']


class _ContextMenuInteractionDataData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    type: Literal[2, 3]
    resolved: NotRequired[ResolvedInteractionDataData]
    guild_id: NotRequired['discord_typings.Snowflake']
    target_id: 'discord_typings.Snowflake'


ApplicationCommandInteractionDataData = Union[
    _ChatInputCommandInteractionDataData, _ContextMenuInteractionDataData
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-message-component-data-structure


class _ButtonComponentInteractionDataData(TypedDict):
    custom_id: str
    component_type: Literal[2]


class _SelectMenuComponentInteractionDataData(TypedDict):
    custom_id: str
    component_type: Literal[3, 5, 6, 7, 8]
    values: NotRequired[List['discord_typings.SelectMenuOptionData']]
    resolved: NotRequired[ResolvedInteractionDataData]


ComponentInteractionDataData = Union[
    _ButtonComponentInteractionDataData, _SelectMenuComponentInteractionDataData
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-modal-submit-data-structure


class ModalSubmitInteractionDataData(TypedDict):
    custom_id: str
    component_type: Literal[4]
    components: List['discord_typings.ActionRowData']


InteractionDataData = Union[
    ApplicationCommandInteractionDataData, ComponentInteractionDataData,
    ModalSubmitInteractionDataData
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-resolved-data-structure


class ResolvedInteractionDataData(TypedDict):
    users: NotRequired[
        Dict['discord_typings.Snowflake', 'discord_typings.UserData']
    ]
    members: NotRequired[
        Dict['discord_typings.Snowflake', 'discord_typings.GuildMemberData']
    ]
    roles: NotRequired[
        Dict['discord_typings.Snowflake', 'discord_typings.RoleData']
    ]
    channels: NotRequired[
        Dict['discord_typings.Snowflake', 'discord_typings.PartialChannelData']
    ]
    messages: NotRequired[
        Dict['discord_typings.Snowflake', 'discord_typings.MessageData']
    ]
    attachments: NotRequired[
        Dict['discord_typings.Snowflake', 'discord_typings.AttachmentData']
    ]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-application-command-interaction-data-option-structure


class _SubcommandOptionInteractionData(TypedDict):
    name: str
    type: Literal[1]
    options: List['discord_typings.ApplicationCommandOptionInteractionData']


class _SubcommandGroupOptionInteractionData(TypedDict):
    name: str
    type: Literal[2]
    options: List['discord_typings.ApplicationCommandOptionInteractionData']


class _StringOptionInteractionData(TypedDict):
    name: str
    type: Literal[3]
    value: str
    focused: NotRequired[bool]


class _IntegerOptionInteractionData(TypedDict):
    name: str
    type: Literal[4]
    value: int
    focused: NotRequired[bool]


class _BooleanOptionInteractionData(TypedDict):
    name: str
    type: Literal[5]
    value: bool


class _UserOptionInteractionData(TypedDict):
    name: str
    type: Literal[6]
    value: 'discord_typings.Snowflake'


class _ChannelOptionInteractionData(TypedDict):
    name: str
    type: Literal[7]
    value: 'discord_typings.Snowflake'


class _RoleOptionInteractionData(TypedDict):
    name: str
    type: Literal[8]
    value: 'discord_typings.Snowflake'


class _MentionableInteractionData(TypedDict):
    name: str
    type: Literal[9]
    value: 'discord_typings.Snowflake'


class _NumberInteractionData(TypedDict):
    name: str
    type: Literal[10]
    value: Union[int, float]
    focused: NotRequired[bool]


class _AttachmentInteractionData(TypedDict):
    name: str
    type: Literal[11]
    value: str


ApplicationCommandOptionInteractionData = Union[
    _SubcommandOptionInteractionData, _SubcommandGroupOptionInteractionData,
    _StringOptionInteractionData, _IntegerOptionInteractionData, _BooleanOptionInteractionData,
    _UserOptionInteractionData, _ChannelOptionInteractionData, _RoleOptionInteractionData,
    _MentionableInteractionData, _NumberInteractionData, _AttachmentInteractionData,
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#message-interaction-object-message-interaction-structure


class MessageInteractionData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: Literal[2, 3, 4]
    name: str
    user: 'discord_typings.UserData'
    member: NotRequired['discord_typings.GuildMemberData']


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-response-structure


class _InteractionNodataResponseData(TypedDict):
    type: Literal[1, 5, 6]


class _InteractionMessageResponseData(TypedDict):
    type: Literal[4, 7]
    data: 'discord_typings.InteractionMessageCallbackData'


class _InteractionAutocompleteResponseData(TypedDict):
    type: Literal[8]
    data: 'discord_typings.InteractionAutocompleteCallbackData[Union[str, int, float]]'


class _InteractionModalResponseData(TypedDict):
    type: Literal[9]
    data: 'discord_typings.InteractionModalCallbackData'


InteractionResponseData = Union[
    _InteractionNodataResponseData, _InteractionMessageResponseData,
    _InteractionAutocompleteResponseData, _InteractionModalResponseData,
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-callback-type


InteractionCallbackTypes = Literal[1, 4, 5, 6, 7, 8, 9]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-callback-data-structure


class InteractionMessageCallbackData(TypedDict):
    tts: NotRequired[bool]
    content: NotRequired[str]
    embeds: NotRequired[List['discord_typings.EmbedData']]
    allowed_mentions: NotRequired['discord_typings.AllowedMentionsData']
    flags: NotRequired[int]
    components: NotRequired[List['discord_typings.ComponentData']]
    attachments: NotRequired[List['discord_typings.PartialAttachmentData']]


class InteractionAutocompleteCallbackData(TypedDict, Generic[_T]):
    choices: List['discord_typings.CommandOptionChoiceData[_T]']


class InteractionModalCallbackData(TypedDict):
    custom_id: str
    title: str
    components: List['discord_typings.ComponentData']


InteractionCallbackData = Union[
    InteractionMessageCallbackData,
    InteractionAutocompleteCallbackData[Union[str, int, float]],
    InteractionModalCallbackData,
]
