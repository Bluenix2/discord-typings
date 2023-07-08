from typing import List, Union

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'ComponentTypes',
    'ActionRowData',
    'ButtonComponentData',
    'ButtonStyles',
    'StringSelectMenuComponentData',
    'UserSelectMenuComponentData',
    'RoleSelectMenuComponentData',
    'MentionableSelectMenuComponentData',
    'ChannelSelectMenuComponentData',
    'SelectMenuComponentData',
    'SelectMenuOptionData',
    'TextInputComponentData',
    'TextInputStyles',
    'ComponentData',
)


# https://discord.com/developers/docs/interactions/message-components#component-object-component-types


ComponentTypes = Literal[1, 2, 3, 4, 5, 6, 7, 8]


# https://discord.com/developers/docs/interactions/message-components#action-rows


class ActionRowData(TypedDict):
    type: Literal[1]
    components: List[Union[
        'discord_typings.ButtonComponentData',
        'discord_typings.SelectMenuComponentData',
        'discord_typings.TextInputComponentData',
    ]]


# https://discord.com/developers/docs/interactions/message-components#button-object-button-structure


# The whole button object itself is split into NonLinkButtonComponent and
# LinkButtonComponent because link buttons need to have the link-style.
class _NonLinkButtonComponentData(TypedDict):
    type: Literal[2]
    style: Literal[1, 2, 3, 4]
    label: NotRequired[str]
    emoji: NotRequired['discord_typings.EmojiData']
    custom_id: str
    disabled: NotRequired[bool]


class _LinkButtonComponentData(TypedDict):
    type: Literal[2]
    style: Literal[5]
    label: NotRequired[str]
    emoji: NotRequired['discord_typings.EmojiData']
    url: str
    disabled: NotRequired[bool]


ButtonComponentData = Union[_NonLinkButtonComponentData, _LinkButtonComponentData]

# https://discord.com/developers/docs/interactions/message-components#button-object-button-styles


ButtonStyles = Literal[1, 2, 3, 4, 5]


# https://discord.com/developers/docs/interactions/message-components#select-menu-object-select-menu-structure


class StringSelectMenuComponentData(TypedDict):
    type: Literal[3]
    custom_id: str
    options: List['discord_typings.SelectMenuOptionData']
    placeholder: NotRequired[str]
    min_values: NotRequired[int]
    max_values: NotRequired[int]
    disabled: NotRequired[bool]


class UserSelectMenuComponentData(TypedDict):
    type: Literal[5]
    custom_id: str
    placeholder: NotRequired[str]
    min_values: NotRequired[int]
    max_values: NotRequired[int]
    disabled: NotRequired[bool]


class RoleSelectMenuComponentData(TypedDict):
    type: Literal[6]
    custom_id: str
    placeholder: NotRequired[str]
    min_values: NotRequired[int]
    max_values: NotRequired[int]
    disabled: NotRequired[bool]


class MentionableSelectMenuComponentData(TypedDict):
    type: Literal[7]
    custom_id: str
    placeholder: NotRequired[str]
    min_values: NotRequired[int]
    max_values: NotRequired[int]
    disabled: NotRequired[bool]


class ChannelSelectMenuComponentData(TypedDict):
    type: Literal[8]
    custom_id: str
    channel_types: List['discord_typings.ChannelTypes']
    placeholder: NotRequired[str]
    min_values: NotRequired[int]
    max_values: NotRequired[int]
    disabled: NotRequired[bool]


SelectMenuComponentData = Union[
    StringSelectMenuComponentData, UserSelectMenuComponentData,
    RoleSelectMenuComponentData, MentionableSelectMenuComponentData,
    ChannelSelectMenuComponentData,
]


# https://discord.com/developers/docs/interactions/message-components#select-menu-object-select-option-structure


class SelectMenuOptionData(TypedDict):
    label: str
    value: str
    description: NotRequired[str]
    emoji: NotRequired['discord_typings.EmojiData']
    default: NotRequired[bool]


# https://discord.com/developers/docs/interactions/message-components#text-inputs-text-input-structure


class TextInputComponentData(TypedDict):
    type: Literal[4]
    custom_id: str
    style: 'discord_typings.TextInputStyles'
    label: str
    min_length: NotRequired[int]
    max_length: NotRequired[int]
    required: NotRequired[bool]
    value: NotRequired[str]
    placeholder: NotRequired[str]


# https://discord.com/developers/docs/interactions/message-components#text-inputs-text-input-styles


TextInputStyles = Literal[1, 2]


ComponentData = Union[
    ActionRowData, ButtonComponentData, SelectMenuComponentData, TextInputComponentData
]
