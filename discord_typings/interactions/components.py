from __future__ import annotations

from typing import List, Literal, TypedDict, Union

from typing_extensions import NotRequired

from ..resources import EmojiData

__all__ = ('ActionRowData', 'ButtonComponentData', 'SelectMenuComponentData', 'ComponentData')


class ActionRowData(TypedDict):
    type: Literal[1]
    components: NotRequired[List[Union[ButtonComponentData, SelectMenuComponentData]]]


# The whole button object itself is split into NonLinkButtonComponent and
# LinkButtonComponent because link buttons need to have the link-style.
class NonLinkButtonComponentData(TypedDict):
    type: Literal[2]
    style: Literal[1, 2, 3, 4]
    label: NotRequired[str]
    emoji: NotRequired[EmojiData]
    custom_id: str
    disabled: NotRequired[bool]


class LinkButtonComponentData(TypedDict):
    type: Literal[2]
    style: Literal[5]
    label: NotRequired[str]
    emoji: NotRequired[EmojiData]
    url: str
    disabled: NotRequired[bool]


ButtonComponentData = Union[NonLinkButtonComponentData, LinkButtonComponentData]


class SelectMenuComponentData(TypedDict):
    type: Literal[3]
    custom_id: str
    options: List[SelectMenuOptionData]
    placeholder: NotRequired[str]
    min_values: NotRequired[int]
    max_values: NotRequired[int]
    disabled: NotRequired[bool]


class SelectMenuOptionData(TypedDict):
    label: str
    value: str
    description: NotRequired[str]
    emoji: NotRequired[EmojiData]
    default: NotRequired[bool]


ComponentData = Union[ActionRowData, ButtonComponentData, SelectMenuComponentData]
