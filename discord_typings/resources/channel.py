from __future__ import annotations

from typing import Any, List, Optional, Union

from typing_extensions import Literal, NotRequired, TypedDict

from ..shared import Snowflake
from .application import ApplicationData
from .emoji import EmojiData
from .guild import GuildMemberData
from .sticker import StickerItemData
from .user import UserData

__all__ = (
    'PartialChannelData', 'TextChannelData', 'NewsChannelData', 'DMChannelData',
    'GroupDMChannelData', 'VoiceChannelData', 'ChannelData', 'MessageData',
    'PermissionOverwriteData', 'ThreadChannelData', 'MessageReferenceData',
    'PermissionOverwriteData', 'ThreadMetadata', 'ThreadMemberData', 'EmbedData',
    'EmbedThumbnailData', 'EmbedVideoData', 'EmbedImageData', 'EmbedProviderData',
    'EmbedAuthorData', 'EmbedFieldData', 'EmbedFooterData', 'AttachmentData',
    'AllowedMentionsData',
)

class PartialChannelData(TypedDict):
    id: Snowflake
    name: str
    type: Literal[0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13]
    permissions: NotRequired[str]


class TextChannelData(TypedDict):
    id: Snowflake
    type: Literal[0]
    guild_id: NotRequired[Snowflake]  # May be missing during guild dispatches
    position: int
    permission_overwrites: List[PermissionOverwriteData]
    name: str
    topic: Optional[str]
    nsfw: bool
    last_message_id: Optional[Snowflake]
    rate_limit_per_user: int
    parent_id: Optional[Snowflake]
    last_pin_timestamp: NotRequired[Optional[str]]
    default_auto_archive_duration: NotRequired[int]


class NewsChannelData(TypedDict):
    id: Snowflake
    type: Literal[5]
    guild_id: NotRequired[Snowflake]  # May be missing during guild dispatches
    position: int
    permission_overwrites: List[PermissionOverwriteData]
    name: str
    topic: Optional[str]
    nsfw: bool
    last_message_id: Optional[Snowflake]
    parent_id: Optional[Snowflake]
    last_pin_timestamp: NotRequired[Optional[str]]
    default_auto_archive_duration: NotRequired[int]


class DMChannelData(TypedDict):
    id: Snowflake
    type: Literal[1]
    last_message_id: Optional[Snowflake]
    recipients: List[UserData]
    last_pin_timestamp: NotRequired[Optional[str]]


class GroupDMChannelData(TypedDict):
    id: Snowflake
    type: Literal[3]
    name: str
    last_message_id: Optional[Snowflake]
    recipients: List[UserData]
    icon: Optional[str]
    owner_id: Snowflake
    application_id: NotRequired[Snowflake]
    last_pin_timestamp: NotRequired[Optional[str]]


class ThreadChannelData(TypedDict):
    id: Snowflake
    type: Literal[10, 11, 12]
    guild_id: NotRequired[Snowflake]
    name: str
    last_message_id: Optional[Snowflake]
    rate_limit_per_user: int
    owner_id: Snowflake
    parent_id: Optional[Snowflake]
    last_pin_timestamp: NotRequired[Optional[str]]
    message_count: int
    member_count: int
    thread_metadata: ThreadMetadata
    member: NotRequired[GuildMemberData]


class VoiceChannelData(TypedDict):
    id: Snowflake
    type: Literal[2, 13]
    guild_id: NotRequired[Snowflake]
    position: int
    permission_overwrites: List[PermissionOverwriteData]
    name: str
    nsfw: bool
    last_message_id: NotRequired[None]
    bitrate: int
    user_limit: int
    parent_id: Optional[Snowflake]
    rtc_region: Optional[str]
    video_quality_mode: NotRequired[Literal[1, 2]]


class CategoryChannelData(TypedDict):
    id: Snowflake
    type: Literal[4]
    guild_id: NotRequired[Snowflake]
    position: int
    permission_overwrites: List[PermissionOverwriteData]
    name: str
    nsfw: bool
    parent_id: Optional[Snowflake]


ChannelData = Union[
    TextChannelData, NewsChannelData, DMChannelData, GroupDMChannelData,
    ThreadChannelData, VoiceChannelData, CategoryChannelData
]


class MessageData(TypedDict):
    id: Snowflake
    channel_id: Snowflake
    guild_id: NotRequired[Snowflake]
    author: UserData
    member: NotRequired[GuildMemberData]
    content: str
    timestamp: str
    edited_timestamp: Optional[str]
    tts: bool
    mention_everyone: bool
    mentions: List[UserMentionData]
    mention_roles: List[Snowflake]
    mention_channels: List[ChannelMentionData]
    attachments: List[AttachmentData]
    embeds: List[EmbedData]
    reactions: List[MessageReactionData]
    nonce: NotRequired[Union[int, str]]
    pinned: bool
    webhook_id: NotRequired[Snowflake]
    type: MessageTypes
    activity: NotRequired[MessageActivityData]
    application: NotRequired[ApplicationData]
    application_id: NotRequired[Snowflake]
    message_reference: NotRequired[MessageReferenceData]
    flags: NotRequired[int]
    references_message: NotRequired[Optional[MessageData]]
    interaction: NotRequired[Any]  # TODO: Interactions
    thread: NotRequired[ThreadChannelData]
    components: NotRequired[List]  # TODO: Interactions
    sticker_items: NotRequired[List[StickerItemData]]


class UserMentionData(UserData):
    member: GuildMemberData


MessageTypes = Literal[
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23
]


class MessageActivityData(TypedDict):
    type: Literal[1, 2, 3, 5]
    party_id: NotRequired[str]


class MessageReferenceData(TypedDict):
    message_id: NotRequired[Snowflake]
    # Note: This will always be sent when receiving a message reference.
    channel_id: NotRequired[Snowflake]
    guild_id: NotRequired[Snowflake]
    fail_if_not_exists: NotRequired[bool]


class FollowedChannelData(TypedDict):
    channel_id: Snowflake
    webhook_id: Snowflake


class MessageReactionData(TypedDict):
    count: int
    me: bool
    emoji: EmojiData


class PermissionOverwriteData(TypedDict):
    id: Snowflake
    type: Literal[0, 1]
    allow: str
    deny: str


class ThreadMetadata(TypedDict):
    archived: bool
    auto_archive_duration: int
    archive_timestamp: str
    locked: bool
    invitable: NotRequired[bool]


class ThreadMemberData(TypedDict):
    id: NotRequired[Snowflake]
    user_id: NotRequired[Snowflake]
    join_timestamp: str
    flags: int


class EmbedData(TypedDict):
    title: NotRequired[str]
    type: NotRequired[Literal['rich', 'image', 'video', 'gifv', 'article', 'link']]
    description: NotRequired[str]
    url: NotRequired[str]
    timestamp: NotRequired[str]
    color: NotRequired[int]
    footer: NotRequired[EmbedFooterData]
    image: NotRequired[EmbedImageData]
    thumbnail: NotRequired[EmbedThumbnailData]
    video: NotRequired[EmbedVideoData]
    provider: NotRequired[EmbedProviderData]
    author: NotRequired[EmbedAuthorData]
    fields: NotRequired[List[EmbedFieldData]]


class EmbedThumbnailData(TypedDict):
    url: str
    proxy_url: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]


class EmbedVideoData(TypedDict):
    url: NotRequired[str]
    proxy_url: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]


class EmbedImageData(TypedDict):
    url: str
    proxy_url: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]


class EmbedProviderData(TypedDict):
    name: NotRequired[str]
    url: NotRequired[str]


class EmbedAuthorData(TypedDict):
    name: str
    url: NotRequired[str]
    icon_url: NotRequired[str]
    proxy_icon_url: NotRequired[str]


class EmbedFooterData(TypedDict):
    text: str
    icon_url: NotRequired[str]
    proxy_icon_url: NotRequired[str]


class EmbedFieldData(TypedDict):
    name: str
    value: str
    inline: NotRequired[bool]


class AttachmentData(TypedDict):
    id: Snowflake
    filename: str
    description: NotRequired[str]
    content_type: NotRequired[str]
    size: int
    url: str
    proxy_url: str
    height: NotRequired[Optional[int]]
    width: NotRequired[Optional[int]]
    ephemeral: NotRequired[bool]


class ChannelMentionData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    type: Literal[0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13]
    name: str


class AllowedMentionsData(TypedDict):
    parse: List[Literal['roles', 'users', 'everyone']]
    roles: List[Snowflake]
    users: List[Snowflake]
    replied_user: bool
