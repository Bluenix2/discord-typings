from __future__ import annotations
from ast import Not

from typing import Dict, List, Literal, TypedDict, Union

from typing_extensions import NotRequired

from discord_typings.resources.channel import (
    AllowedMentionsData, AttachmentData, EmbedData
)

from ..resources import (
    ChannelData, GuildMemberData, MessageData, RoleData, UserData
)
from ..shared import Snowflake
from .commands import (
    ApplicationCommandOptionInteractionData, AutocompleteOptionData,
    SubcommandGroupOptionInteractionData, SubcommandOptionInteractionData
)
from .components import ComponentData, SelectMenuOptionData

__all__ = (
    'InteractionData', 'ResolvedInteractionData', 'MessageInteractionData',
    'InteractionResponseData'
)


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-interaction-structure


class GuildInteractionData(TypedDict):
    id: Snowflake
    application_id: Snowflake
    # type: Literal[2, 3, 4]
    # data: InteractionDataData
    guild_id: Snowflake
    channel_id: Snowflake
    member: GuildMemberData
    token: str
    version: int
    # message: NotRequired[MessageData]
    locale: str
    guild_locale: str


class ApplicationCommandGuildInteractionData(GuildInteractionData):
    type: Literal[2]
    data: ApplicationCommandInteractionDataData


class ComponentGuildInteractionData(GuildInteractionData):
    type: Literal[3]
    data: ComponentInteractionDataData
    message: MessageData


class AutocompleteGuildInteractionData(GuildInteractionData):
    type: Literal[4]


class ChannelInteractionData(TypedDict):
    id: Snowflake
    application_id: Snowflake
    # type: Literal[2, 3, 4]
    # data: InteractionDataData
    channel_id: Snowflake
    user: UserData
    token: str
    version: int
    # message: NotRequired[MessageData]
    locale: str


class ApplicationCommandChannelInteractionData(ChannelInteractionData):
    type: Literal[2]
    data: ApplicationCommandInteractionDataData


class ComponentChannelInteractionData(ChannelInteractionData):
    type: Literal[3]
    data: ComponentInteractionDataData
    message: MessageData


class AutocompleteChannelInteractionData(ChannelInteractionData):
    type: Literal[4]


class UserCommandInteractionData(TypedDict):
    id: Snowflake
    application_id: Snowflake
    type: Literal[2]
    data: ApplicationCommandInteractionDataData
    # member: NotRequired[GuildMemberData]
    # user: NotRequired[UserData]
    token: str
    version: int
    locale: str
    # guild_locale: NotRequired[str]


class GuildUserCommandInteractionData(UserCommandInteractionData):
    member: GuildMemberData
    guild_locale: str


class ChanneluserCommandInteractionData(UserCommandInteractionData):
    user: UserData


InteractionData = Union[
    ApplicationCommandGuildInteractionData, ComponentGuildInteractionData,
    AutocompleteGuildInteractionData, ApplicationCommandChannelInteractionData,
    ComponentChannelInteractionData, AutocompleteChannelInteractionData,
    GuildUserCommandInteractionData, ChanneluserCommandInteractionData
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-interaction-data-structure


class ApplicationCommandInteractionDataData(TypedDict):
    id: Snowflake
    name: str
    type: Literal[1, 2, 3]
    resolved: NotRequired[ResolvedInteractionData]
    options: NotRequired[
        Union[
            SubcommandOptionInteractionData,
            SubcommandGroupOptionInteractionData,
            ApplicationCommandOptionInteractionData
        ]
    ]


class ButtonComponentInteractionDataData(TypedDict):
    custom_id: str
    component_type: Literal[2]


class SelectComponentInteractionDataData(TypedDict):
    custom_id: str
    component_type: Literal[3]
    values: List[SelectMenuOptionData]


ComponentInteractionDataData = Union[
    ButtonComponentInteractionDataData, SelectComponentInteractionDataData
]


class ContextMenuInteractionDataData(ApplicationCommandInteractionDataData):
    target_id: Snowflake


InteractionDataData = Union[
    ApplicationCommandInteractionDataData, ButtonComponentInteractionDataData,
    SelectComponentInteractionDataData, ContextMenuInteractionDataData
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-resolved-data-structure


class ResolvedInteractionData(TypedDict):
    users: Dict[Snowflake, UserData]
    members: Dict[Snowflake, GuildMemberData]
    roles: Dict[Snowflake, RoleData]
    channels: Dict[Snowflake, ChannelData]
    messages: Dict[Snowflake, MessageData]


# https://discord.com/developers/docs/interactions/receiving-and-responding#message-interaction-object-message-interaction-structure


class MessageInteractionData(TypedDict):
    id: Snowflake
    type: Literal[2, 3, 4]
    name: str
    user: UserData


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-response-structure


class InteractionMessageResponseInnerData(TypedDict):
    tts: NotRequired[bool]
    content: NotRequired[str]
    embeds: NotRequired[List[EmbedData]]
    allowed_mentions: NotRequired[AllowedMentionsData]
    flags: NotRequired[int]
    components: NotRequired[List[ComponentData]]
    attachments: NotRequired[List[AttachmentData]]


class InteractionMessageResponseData(TypedDict):
    type: Literal[4, 7]
    data: InteractionMessageResponseInnerData

    
class InteractionAutocompleteResponseData(TypedDict):
    type: Literal[8]
    data: InteractionAutocompleteCallbackData


class InteractionNodataResponseData(TypedDict):
    type: Literal[1, 5, 6]


InteractionResponseData = Union[
    InteractionMessageResponseData, InteractionAutocompleteResponseData,
    InteractionNodataResponseData
]


# https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-callback-data-structure



class InteractionMessageCallbackData(TypedDict):
    tts: NotRequired[bool]
    content: NotRequired[str]
    embeds: NotRequired[List[EmbedData]]
    allowed_mentions: NotRequired[AllowedMentionsData]
    flags: NotRequired[int]
    components: NotRequired[ComponentData]
    attachments: NotRequired[AttachmentData]


class InteractionAutocompleteCallbackData(TypedDict):
    choices: List[AutocompleteOptionData]
