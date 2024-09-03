from typing import List, Optional

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'PollData',
    'PollCreateRequestData',
    'PollLayoutType',
    'PollMediaData',
    'PollAnswerData',
    'PollResultsData',
    'PollAnswerCountData',
)


# https://discord.com/developers/docs/resources/poll#poll-object-poll-object-structure


class PollData(TypedDict):
    question: 'discord_typings.PollMediaData'
    answers: List['discord_typings.PollAnswerData']
    expiry: Optional[str]
    allow_multiselect: bool
    layout_type: 'discord_typings.PollLayoutType'
    results: NotRequired['discord_typings.PollResultsData']


# https://discord.com/developers/docs/resources/poll#poll-create-request-object-poll-create-request-object-structure


class PollCreateRequestData(TypedDict):
    question: 'discord_typings.PollMediaData'
    answers: List['discord_typings.PollAnswerData']
    duration: int
    allow_multiselect: bool
    layout_type: NotRequired['discord_typings.PollLayoutType']


# https://discord.com/developers/docs/resources/poll#layout-type


PollLayoutType = Literal[1]


# https://discord.com/developers/docs/resources/poll#poll-media-object-poll-media-object-structure


class PollMediaData(TypedDict):
    text: NotRequired[str]
    emoji: NotRequired['discord_typings.EmojiData']


# https://discord.com/developers/docs/resources/poll#poll-answer-object-poll-answer-object-structure


class PollAnswerData(TypedDict):
    answer_id: int
    poll_media: 'discord_typings.PollMediaData'


# https://discord.com/developers/docs/resources/poll#poll-results-object-poll-results-object-structure


class PollResultsData(TypedDict):
    is_finalized: bool
    answer_counts: List['discord_typings.PollAnswerCountData']


# https://discord.com/developers/docs/resources/poll#poll-results-object-poll-answer-count-object-structure


class PollAnswerCountData(TypedDict):
    id: int
    count: int
    me_voted: bool
