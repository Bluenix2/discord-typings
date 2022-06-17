from __future__ import annotations

from typing import TYPE_CHECKING, List, Union

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from ..resources import EmojiData

__all__ = (
    'ComponentTypes', 'ActionRowData', 'ButtonComponentData', 'ButtonStyles',
    'SelectMenuComponentData', 'SelectMenuOptionData', 'TextInputComponentData',
    'ComponentData'
)


# https://discord.com/developers/docs/interactions/message-components#component-object-component-types


ComponentTypes = Literal[1, 2, 3, 4]


# https://discord.com/developers/docs/interactions/message-components#action-rows


@final
class ActionRowData(TypedDict):
    type: Literal[1]
    components: List[Union[ButtonComponentData, SelectMenuComponentData]]


# https://discord.com/developers/docs/interactions/message-components#button-object-button-structure


# The whole button object itself is split into NonLinkButtonComponent and
# LinkButtonComponent because link buttons need to have the link-style.
@final
class NonLinkButtonComponentData(TypedDict):
    type: Literal[2]
    style: Literal[1, 2, 3, 4]
    label: NotRequired[str]
    emoji: NotRequired[EmojiData]
    custom_id: str
    disabled: NotRequired[bool]


@final
class LinkButtonComponentData(TypedDict):
    type: Literal[2]
    style: Literal[5]
    label: NotRequired[str]
    emoji: NotRequired[EmojiData]
    url: str
    disabled: NotRequired[bool]


ButtonComponentData = Union[NonLinkButtonComponentData, LinkButtonComponentData]

# https://discord.com/developers/docs/interactions/message-components#button-object-button-styles


ButtonStyles = Literal[1, 2, 3, 4, 5]


# https://discord.com/developers/docs/interactions/message-components#select-menu-object-select-menu-structure


@final
class SelectMenuComponentData(TypedDict):
    type: Literal[3]
    custom_id: str
    options: List[SelectMenuOptionData]
    placeholder: NotRequired[str]
    min_values: NotRequired[int]
    max_values: NotRequired[int]
    disabled: NotRequired[bool]


# https://discord.com/developers/docs/interactions/message-components#select-menu-object-select-option-structure


@final
class SelectMenuOptionData(TypedDict):
    label: str
    value: str
    description: NotRequired[str]
    emoji: NotRequired[EmojiData]
    default: NotRequired[bool]


# https://discord.com/developers/docs/interactions/message-components#text-inputs-text-input-structure


@final
class TextInputComponentData(TypedDict):
    type: Literal[4]
    custom_id: str
    style: TextInputStyles
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
