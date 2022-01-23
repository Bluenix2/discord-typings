from __future__ import annotations

from typing import List, Literal, TypedDict, TypeVar, Union

from typing_extensions import NotRequired

from ..shared import Snowflake

__all__ = (
    'ApplicationCommandData', 'SubcommandOptionData', 'SubcommandGroupOptionData',
    'AutocompleteOptionData', 'ApplicationCommandOptionData',
    'ApplicationCommandOptionInteractionData'
)


T = TypeVar('T')


class ChatInputCommandData(TypedDict):
    id: Snowflake
    type: NotRequired[Literal[1]]
    application_id: Snowflake
    guild_id: NotRequired[Snowflake]
    name: str
    description: str
    options: List[ApplicationCommandOptionData]
    default_permission: NotRequired[bool]
    version: Snowflake


class ContextMenuCommandData(TypedDict):
    id: Snowflake
    type: NotRequired[Literal[2, 3]]
    application_id: Snowflake
    guild_id: NotRequired[Snowflake]
    name: str
    description: str
    default_permission: NotRequired[bool]
    version: Snowflake


ApplicationCommandData = Union[ChatInputCommandData, ContextMenuCommandData]


# The variations and overloads of options are huge, but we want to provide
# extremely accurate typing - this is gonna be a huge Union with a lot of
# TypedDict subclasses...


class SubcommandOptionData(TypedDict):
    type: Literal[1]
    name: str
    description: str
    options: NotRequired[List[ApplicationCommandOptionData]]


class SubcommandGroupOptionData(TypedDict):
    type: Literal[2]
    name: str
    description: str
    options: List[SubcommandOptionData]


class ChoicesStringOptionData(TypedDict):
    type: Literal[3]
    name: str
    description: str
    required: NotRequired[bool]
    choices: NotRequired[List[StrCommandOptionChoiceData]]


class AutocompleteStringOptionData(TypedDict):
    type: Literal[3]
    name: str
    description: str
    required: NotRequired[bool]
    autocomplete: NotRequired[bool]


class ChoicesIntegerCommandOptionData(TypedDict):
    type: Literal[4]
    name: str
    description: str
    required: NotRequired[bool]
    choices: NotRequired[List[IntCommandOptionChoiceData]]


class MinMaxIntegerCommandOptionData(TypedDict):
    type: Literal[4]
    name: str
    description: str
    required: NotRequired[bool]
    min_value: NotRequired[int]
    max_value: NotRequired[int]


class AutocompleteIntegerOptionData(TypedDict):
    type: Literal[4]
    name: str
    description: str
    required: NotRequired[bool]
    autocomplete: NotRequired[bool]


class BooleanOptionData(TypedDict):
    type: Literal[5]
    name: str
    description: str
    required: NotRequired[bool]


class UserOptionData(TypedDict):
    type: Literal[6]
    name: str
    description: str
    required: NotRequired[bool]


class ChannelOptionData(TypedDict):
    type: Literal[7]
    name: str
    description: str
    required: NotRequired[bool]
    channel_types: NotRequired[List[Literal[0, 2, 4, 5, 6, 13]]]


class RoleOptionData(TypedDict):
    type: Literal[8]
    name: str
    description: str
    required: NotRequired[bool]


class MentionableOptionData(TypedDict):
    type: Literal[9]
    name: str
    description: str
    required: NotRequired[bool]


class ChoicesNumberCommandOptionData(TypedDict):
    type: Literal[4]
    name: str
    description: str
    required: NotRequired[bool]
    choices: NotRequired[List[NumberCommandOptionChoiceData]]


class MinMaxNumberCommandOptionData(TypedDict):
    type: Literal[4]
    name: str
    description: str
    required: NotRequired[bool]
    min_value: NotRequired[Union[int, float]]
    max_value: NotRequired[Union[int, float]]


class AutocompleteNumberOptionData(TypedDict):
    type: Literal[4]
    name: str
    description: str
    required: NotRequired[bool]
    autocomplete: NotRequired[bool]


AutocompleteOptionData = Union[
    AutocompleteStringOptionData, AutocompleteIntegerOptionData,
    AutocompleteNumberOptionData
]


ApplicationCommandOptionData = Union[
    ChoicesStringOptionData, ChoicesIntegerCommandOptionData,
    MinMaxIntegerCommandOptionData, BooleanOptionData,
    UserOptionData, ChannelOptionData, RoleOptionData, MentionableOptionData,
    ChoicesNumberCommandOptionData, MinMaxNumberCommandOptionData,
    AutocompleteOptionData,
]


class StrCommandOptionChoiceData(TypedDict):
    name: str
    value: str


class IntCommandOptionChoiceData(TypedDict):
    name: str
    value: int


class NumberCommandOptionChoiceData(TypedDict):
    name: str
    value: Union[int, float]

class SubcommandOptionInteractionData(TypedDict):
    name: str
    type: Literal[1]
    options: List[ApplicationCommandOptionInteractionData]


class SubcommandGroupOptionInteractionData(TypedDict):
    name: str
    type: Literal[2]
    options: List[SubcommandOptionInteractionData]


class StringOptionInteractionData(TypedDict):
    name: str
    type: Literal[3]
    value: str
    focused: NotRequired[bool]


class IntegerOptionInteractionData(TypedDict):
    name: str
    type: Literal[4]
    value: int
    focused: NotRequired[bool]


class BooleanOptionInteractionData(TypedDict):
    name: str
    type: Literal[5]
    value: bool


class UserOptionInteractionData(TypedDict):
    name: str
    type: Literal[6]
    value: Snowflake


class ChannelOptionInteractionData(TypedDict):
    name: str
    type: Literal[7]
    value: Snowflake


class RoleOptionInteractionData(TypedDict):
    name: str
    type: Literal[8]
    value: Snowflake


class MentionableInteractionData(TypedDict):
    name: str
    type: Literal[9]
    value: Snowflake


class NumberInteractionData(TypedDict):
    name: str
    type: Literal[10]
    value: Union[int, float]
    focused: NotRequired[bool]


ApplicationCommandOptionInteractionData = Union[
    SubcommandOptionInteractionData, SubcommandGroupOptionInteractionData,
    StringOptionInteractionData, IntegerOptionInteractionData, BooleanOptionInteractionData,
    UserOptionInteractionData, ChannelOptionInteractionData, RoleOptionInteractionData,
    MentionableInteractionData, NumberInteractionData,
]
