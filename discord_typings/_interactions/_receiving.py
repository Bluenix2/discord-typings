from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from .._reference import Snowflake
    from .._resources import (
        AllowedMentionsData, AttachmentData, EmbedData, GuildMemberData,
        MessageData, PartialAttachmentData, PartialChannelData, RoleData,
        UserData
    )
    from ._commands import AutocompleteOptionData, Locales
    from ._components import ActionRowData, ComponentData, SelectMenuOptionData

__all__ = (
    'InteractionData', 'InteractionType', 'ResolvedInteractionDataData',
    'MessageInteractionData', 'InteractionResponseData', 'InteractionCallbackTypes',
    'InteractionCallbackData', 'ApplicationCommandInteractionData',
    'ComponentInteractionData', 'AutocompleteInteractionData', 'InteractionData',
    'InteractionMessageCallbackData', 'InteractionAutocompleteCallbackData',
    'InteractionModalCallbackData', 'InteractionMessageResponseData',
    'InteractionAutocompleteResponseData', 'InteractionModalResponseData',
    'InteractionNodataResponseData', 'ModalInteractionData',
    'ApplicationCommandOptionInteractionData', 'SelectMenuComponentInteractionDataData',
    'ButtonComponentInteractionDataData', 'ChatInputCommandInteractionDataData',
    'ContextMenuInteractionDataData', 'ComponentInteractionDataData',
    'InteractionDataData'
)


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-interaction-structure


class GuildInteractionData(TypedDict):
    id: Snowflake
    application_id: Snowflake
    guild_id: Snowflake
    channel_id: Snowflake
    member: GuildMemberData
    token: str
    version: int
    locale: Locales
    guild_locale: Locales


@final
class ApplicationCommandGuildInteractionData(GuildInteractionData):
    type: Literal[2]
    data: ApplicationCommandInteractionDataData
    app_permissions: str


@final
class ComponentGuildInteractionData(GuildInteractionData):
    type: Literal[3]
    data: ComponentInteractionDataData
    message: MessageData
    app_permissions: str


@final
class AutocompleteGuildInteractionData(GuildInteractionData):
    type: Literal[4]
    data: ApplicationCommandInteractionDataData


@final
class ModalGuildInteractionData(GuildInteractionData):
    type: Literal[5]
    data: ModalSubmitInteractionDataData
    message: MessageData
    app_permissions: str


class ChannelInteractionData(TypedDict):
    id: Snowflake
    application_id: Snowflake
    channel_id: Snowflake
    user: UserData
    token: str
    version: int
    locale: Locales


@final
class ApplicationCommandChannelInteractionData(ChannelInteractionData):
    type: Literal[2]
    data: Union[ApplicationCommandInteractionDataData, ContextMenuInteractionDataData]


@final
class ComponentChannelInteractionData(ChannelInteractionData):
    type: Literal[3]
    data: ComponentInteractionDataData
    message: MessageData


@final
class AutocompleteChannelInteractionData(ChannelInteractionData):
    type: Literal[4]
    data: ApplicationCommandInteractionDataData


@final
class ModalChannelInteractionData(ChannelInteractionData):
    type: Literal[5]
    data: ModalSubmitInteractionDataData
    message: MessageData


ApplicationCommandInteractionData = Union[
    ApplicationCommandGuildInteractionData, ApplicationCommandChannelInteractionData,
]


ComponentInteractionData = Union[
    ComponentGuildInteractionData, ComponentChannelInteractionData
]


ModalInteractionData = Union[
    ModalGuildInteractionData, ModalChannelInteractionData
]

AutocompleteInteractionData = Union[
    AutocompleteGuildInteractionData, AutocompleteChannelInteractionData
]


InteractionData = Union[
    ApplicationCommandInteractionData, ComponentInteractionData, AutocompleteInteractionData,
    ModalInteractionData,
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-interaction-type


InteractionType = Literal[1, 2, 3, 4, 5]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-application-command-data-structure


@final
class ChatInputCommandInteractionDataData(TypedDict):
    id: Snowflake
    name: str
    type: Literal[1]
    resolved: NotRequired[ResolvedInteractionDataData]
    options: NotRequired[List[ApplicationCommandOptionInteractionData]]
    guild_id: NotRequired[Snowflake]


@final
class ContextMenuInteractionDataData(TypedDict):
    id: Snowflake
    name: str
    type: Literal[2, 3]
    resolved: NotRequired[ResolvedInteractionDataData]
    guild_id: NotRequired[Snowflake]
    target_id: Snowflake


ApplicationCommandInteractionDataData = Union[
    ChatInputCommandInteractionDataData, ContextMenuInteractionDataData
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-message-component-data-structure


@final
class ButtonComponentInteractionDataData(TypedDict):
    custom_id: str
    component_type: Literal[2]


@final
class SelectMenuComponentInteractionDataData(TypedDict):
    custom_id: str
    component_type: Literal[3, 5, 6, 7, 8]
    values: NotRequired[List[SelectMenuOptionData]]
    resolved: NotRequired[ResolvedInteractionDataData]


ComponentInteractionDataData = Union[
    ButtonComponentInteractionDataData, SelectMenuComponentInteractionDataData
]

# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-modal-submit-data-structure


@final
class ModalSubmitInteractionDataData(TypedDict):
    custom_id: str
    component_type: Literal[4]
    components: List[ActionRowData]


InteractionDataData = Union[
    ApplicationCommandInteractionDataData, ComponentInteractionDataData,
    ModalSubmitInteractionDataData
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-resolved-data-structure


@final
class ResolvedInteractionDataData(TypedDict):
    users: NotRequired[Dict[Snowflake, UserData]]
    members: NotRequired[Dict[Snowflake, GuildMemberData]]
    roles: NotRequired[Dict[Snowflake, RoleData]]
    channels: NotRequired[Dict[Snowflake, PartialChannelData]]
    messages: NotRequired[Dict[Snowflake, MessageData]]
    attachments: NotRequired[Dict[Snowflake, AttachmentData]]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-application-command-interaction-data-option-structure


@final
class SubcommandOptionInteractionData(TypedDict):
    name: str
    type: Literal[1]
    options: List[ApplicationCommandOptionInteractionData]


@final
class SubcommandGroupOptionInteractionData(TypedDict):
    name: str
    type: Literal[2]
    options: List[SubcommandOptionInteractionData]


@final
class StringOptionInteractionData(TypedDict):
    name: str
    type: Literal[3]
    value: str
    focused: NotRequired[bool]


@final
class IntegerOptionInteractionData(TypedDict):
    name: str
    type: Literal[4]
    value: int
    focused: NotRequired[bool]


@final
class BooleanOptionInteractionData(TypedDict):
    name: str
    type: Literal[5]
    value: bool


@final
class UserOptionInteractionData(TypedDict):
    name: str
    type: Literal[6]
    value: Snowflake


@final
class ChannelOptionInteractionData(TypedDict):
    name: str
    type: Literal[7]
    value: Snowflake


@final
class RoleOptionInteractionData(TypedDict):
    name: str
    type: Literal[8]
    value: Snowflake


@final
class MentionableInteractionData(TypedDict):
    name: str
    type: Literal[9]
    value: Snowflake


@final
class NumberInteractionData(TypedDict):
    name: str
    type: Literal[10]
    value: Union[int, float]
    focused: NotRequired[bool]


@final
class AttachmentInteractionData(TypedDict):
    name: str
    type: Literal[11]
    value: str


ApplicationCommandOptionInteractionData = Union[
    SubcommandOptionInteractionData, SubcommandGroupOptionInteractionData,
    StringOptionInteractionData, IntegerOptionInteractionData, BooleanOptionInteractionData,
    UserOptionInteractionData, ChannelOptionInteractionData, RoleOptionInteractionData,
    MentionableInteractionData, NumberInteractionData, AttachmentInteractionData,
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#message-interaction-object-message-interaction-structure


@final
class MessageInteractionData(TypedDict):
    id: Snowflake
    type: Literal[2, 3, 4]
    name: str
    user: UserData
    member: NotRequired[GuildMemberData]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-response-structure


@final
class InteractionNodataResponseData(TypedDict):
    type: Literal[1, 5, 6]


@final
class InteractionMessageResponseData(TypedDict):
    type: Literal[4, 7]
    data: InteractionMessageCallbackData


@final
class InteractionAutocompleteResponseData(TypedDict):
    type: Literal[8]
    data: InteractionAutocompleteCallbackData


@final
class InteractionModalResponseData(TypedDict):
    type: Literal[9]
    data: InteractionModalCallbackData


InteractionResponseData = Union[
    InteractionNodataResponseData, InteractionMessageResponseData,
    InteractionAutocompleteResponseData, InteractionModalResponseData,
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-callback-type


InteractionCallbackTypes = Literal[1, 4, 5, 6, 7, 8, 9]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-callback-data-structure


@final
class InteractionMessageCallbackData(TypedDict):
    tts: NotRequired[bool]
    content: NotRequired[str]
    embeds: NotRequired[List[EmbedData]]
    allowed_mentions: NotRequired[AllowedMentionsData]
    flags: NotRequired[int]
    components: NotRequired[List[ComponentData]]
    attachments: NotRequired[List[PartialAttachmentData]]


@final
class InteractionAutocompleteCallbackData(TypedDict):
    choices: List[AutocompleteOptionData]


@final
class InteractionModalCallbackData(TypedDict):
    custom_id: str
    title: str
    components: List[ActionRowData]


InteractionCallbackData = Union[
    InteractionMessageCallbackData, InteractionAutocompleteCallbackData,
    InteractionModalCallbackData
]
