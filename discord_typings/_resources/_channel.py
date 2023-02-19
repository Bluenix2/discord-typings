from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from typing_extensions import Literal, NotRequired, TypedDict, final

from ._user import UserBase  # Subclassed for UserMentionData

if TYPE_CHECKING:
    from .._interactions import ComponentData, MessageInteractionData
    from .._reference import Snowflake
    from ._application import ApplicationData
    from ._emoji import EmojiData
    from ._guild import GuildMemberData
    from ._sticker import StickerItemData
    from ._user import UserData

__all__ = (
    'PartialChannelData', 'TextChannelData', 'NewsChannelData', 'DMChannelData',
    'GroupDMChannelData', 'VoiceChannelData', 'CategoryChannelData',
    'ChannelData', 'ChannelTypes', 'VideoQualityModes', 'ChannelMessageData',
    'GuildMessageData', 'MessageData', 'UserMentionData', 'MessageTypes',
    'MessageActivityData', 'MessageActivityTypes', 'PermissionOverwriteData',
    'ThreadChannelData', 'MessageReferenceData', 'FollowedChannelData',
    'PermissionOverwriteData', 'ThreadMetadataData', 'ThreadMemberData', 'EmbedData',
    'EmbedThumbnailData', 'EmbedVideoData', 'EmbedImageData',
    'EmbedProviderData', 'EmbedAuthorData', 'EmbedFieldData', 'EmbedFooterData',
    'PartialAttachmentData', 'AttachmentData', 'AllowedMentionsData', 'HasMoreListThreadsData',
    'ChannelMentionData', 'MessageReactionData', 'DefaultReactionData',
    'ForumTagData', 'ForumChannelData', 'SortOrderTypes', 'RoleSubscriptionData',
)


# https://discord.com/developers/docs/resources/channel#channel-object-channel-structure


@final
class PartialChannelData(TypedDict):
    id: Snowflake
    name: str
    type: Literal[0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13]
    permissions: NotRequired[str]


@final
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
    flags: int


@final
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
    flags: int


@final
class DMChannelData(TypedDict):
    id: Snowflake
    type: Literal[1]
    last_message_id: Optional[Snowflake]
    recipients: List[UserData]
    last_pin_timestamp: NotRequired[Optional[str]]
    flags: int


@final
class GroupDMChannelData(TypedDict):
    id: Snowflake
    type: Literal[3]
    name: str
    last_message_id: Optional[Snowflake]
    recipients: List[UserData]
    icon: Optional[str]
    owner_id: Snowflake
    application_id: NotRequired[Snowflake]
    managed: bool
    last_pin_timestamp: NotRequired[Optional[str]]
    flags: int


@final
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
    thread_metadata: ThreadMetadataData
    member: NotRequired[ThreadMemberData]
    flags: int
    total_messages_sent: int
    applied_tags: NotRequired[List[Snowflake]]


@final
class VoiceChannelData(TypedDict):
    id: Snowflake
    type: Literal[2, 13]
    guild_id: NotRequired[Snowflake]
    position: int
    permission_overwrites: List[PermissionOverwriteData]
    name: str
    nsfw: bool
    last_message_id: NotRequired[Optional[Snowflake]]
    bitrate: int
    user_limit: int
    parent_id: Optional[Snowflake]
    last_pin_timestamp: NotRequired[Optional[str]]
    rtc_region: Optional[str]
    video_quality_mode: NotRequired[VideoQualityModes]
    flags: int


@final
class CategoryChannelData(TypedDict):
    id: Snowflake
    type: Literal[4]
    guild_id: NotRequired[Snowflake]
    position: int
    permission_overwrites: List[PermissionOverwriteData]
    name: str
    nsfw: bool
    flags: int


@final
class ForumChannelData(TypedDict):
    id: Snowflake
    type: Literal[15]
    guild_id: NotRequired[Snowflake]
    position: int
    permission_overwrites: List[PermissionOverwriteData]
    name: str
    topic: Optional[str]
    nsfw: bool
    last_message_id: Optional[Snowflake]
    rate_limit_per_user: int
    default_auto_archive_duration: NotRequired[int]
    flags: int
    available_tags: List[ForumTagData]
    default_reaction_emoji: Optional[DefaultReactionData]
    default_thread_rate_limit_per_user: int
    default_sort_order: Optional[SortOrderTypes]
    default_forum_layout: ForumLayoutTypes


ChannelData = Union[
    TextChannelData, NewsChannelData, DMChannelData, GroupDMChannelData,
    ThreadChannelData, VoiceChannelData, CategoryChannelData, ForumChannelData
]


# https://discord.com/developers/docs/resources/channel#channel-object-channel-types


ChannelTypes = Literal[0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]


# https://discord.com/developers/docs/resources/channel#channel-object-video-quality-modes


VideoQualityModes = Literal[1, 2]


# https://discord.com/developers/docs/resources/channel#channel-object-sort-order-types


SortOrderTypes = Literal[0, 1]


# https://discord.com/developers/docs/resources/channel#channel-object-forum-layout-types


ForumLayoutTypes = Literal[0, 1, 2]


# https://discord.com/developers/docs/resources/channel#message-object-message-structure


class MessageBase(TypedDict):
    id: Snowflake
    channel_id: Snowflake
    author: UserData
    content: str
    timestamp: str
    edited_timestamp: Optional[str]
    tts: bool
    mention_everyone: bool
    mentions: Union[List[UserData], List[UserMentionData]]
    mention_roles: List[Snowflake]
    mention_channels: NotRequired[List[ChannelMentionData]]
    attachments: List[AttachmentData]
    embeds: List[EmbedData]
    reactions: NotRequired[List[MessageReactionData]]
    nonce: NotRequired[Union[int, str]]
    pinned: bool
    webhook_id: NotRequired[Snowflake]
    type: MessageTypes
    activity: NotRequired[MessageActivityData]
    application: NotRequired[ApplicationData]
    application_id: NotRequired[Snowflake]
    message_reference: NotRequired[MessageReferenceData]
    flags: NotRequired[int]
    referenced_message: NotRequired[Optional[MessageData]]
    interaction: NotRequired[MessageInteractionData]
    thread: NotRequired[ThreadChannelData]
    components: NotRequired[List[ComponentData]]
    sticker_items: NotRequired[List[StickerItemData]]
    position: NotRequired[int]
    role_subscription_data: NotRequired[RoleSubscriptionData]


@final
class ChannelMessageData(MessageBase):
    pass


@final
class GuildMessageData(MessageBase):
    guild_id: Snowflake
    member: GuildMemberData


MessageData = Union[ChannelMessageData, GuildMessageData]


@final
class UserMentionData(UserBase):
    member: GuildMemberData


# https://discord.com/developers/docs/resources/channel#message-object-message-types


MessageTypes = Literal[
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
]


# https://discord.com/developers/docs/resources/channel#message-object-message-activity-structure


@final
class MessageActivityData(TypedDict):
    type: MessageActivityTypes
    party_id: NotRequired[str]


# https://discord.com/developers/docs/resources/channel#message-object-message-activity-types


MessageActivityTypes = Literal[1, 2, 3, 5]


# https://discord.com/developers/docs/resources/channel#message-reference-object-message-reference-structure


@final
class MessageReferenceData(TypedDict):
    message_id: NotRequired[Snowflake]
    # Note: This will always be sent when receiving a message reference.
    channel_id: NotRequired[Snowflake]
    guild_id: NotRequired[Snowflake]
    fail_if_not_exists: NotRequired[bool]


# https://discord.com/developers/docs/resources/channel#followed-channel-object-followed-channel-structure


@final
class FollowedChannelData(TypedDict):
    channel_id: Snowflake
    webhook_id: Snowflake


# https://discord.com/developers/docs/resources/channel#reaction-object-reaction-structure


@final
class MessageReactionData(TypedDict):
    count: int
    me: bool
    emoji: EmojiData


# https://discord.com/developers/docs/resources/channel#overwrite-object-overwrite-structure


@final
class PermissionOverwriteData(TypedDict):
    id: Snowflake
    type: Literal[0, 1]
    allow: str
    deny: str


# https://discord.com/developers/docs/resources/channel#thread-metadata-object-thread-metadata-structure


@final
class ThreadMetadataData(TypedDict):
    archived: bool
    auto_archive_duration: int
    archive_timestamp: str
    locked: bool
    invitable: NotRequired[bool]
    create_timestamp: NotRequired[Optional[str]]


# https://discord.com/developers/docs/resources/channel#thread-member-object-thread-member-structure


@final
class ThreadMemberData(TypedDict):
    id: NotRequired[Snowflake]
    user_id: NotRequired[Snowflake]
    member: NotRequired[GuildMemberData]
    join_timestamp: str
    flags: int


# https://discord.com/developers/docs/resources/channel#default-reaction-object-default-reaction-structure


@final
class DefaultReactionData(TypedDict):
    emoji_name: Optional[str]
    emoji_id: Optional[Snowflake]


# https://discord.com/developers/docs/resources/channel#forum-tag-object-forum-tag-structure


@final
class ForumTagData(TypedDict):
    id: Snowflake
    name: str
    moderated: bool
    emoji_id: Optional[Snowflake]
    emoji_name: Optional[Snowflake]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-structure


@final
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


# https://discord.com/developers/docs/resources/channel#embed-object-embed-thumbnail-structure


@final
class EmbedThumbnailData(TypedDict):
    url: str
    proxy_url: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-video-structure


@final
class EmbedVideoData(TypedDict):
    url: NotRequired[str]
    proxy_url: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-image-structure


@final
class EmbedImageData(TypedDict):
    url: str
    proxy_url: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-provider-structure


@final
class EmbedProviderData(TypedDict):
    name: NotRequired[str]
    url: NotRequired[str]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-author-structure


@final
class EmbedAuthorData(TypedDict):
    name: str
    url: NotRequired[str]
    icon_url: NotRequired[str]
    proxy_icon_url: NotRequired[str]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-footer-structure


@final
class EmbedFooterData(TypedDict):
    text: str
    icon_url: NotRequired[str]
    proxy_icon_url: NotRequired[str]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-field-structure


@final
class EmbedFieldData(TypedDict):
    name: str
    value: str
    inline: NotRequired[bool]


# https://discord.com/developers/docs/resources/channel#attachment-object-attachment-structure


@final
class PartialAttachmentData(TypedDict):
    id: Snowflake
    filename: NotRequired[str]
    description: NotRequired[str]


@final
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


# https://discord.com/developers/docs/resources/channel#channel-mention-object-channel-mention-structure


@final
class ChannelMentionData(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    type: Literal[0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13]
    name: str


# https://discord.com/developers/docs/resources/channel#allowed-mentions-object-allowed-mentions-structure


@final
class AllowedMentionsData(TypedDict):
    parse: NotRequired[List[Literal['roles', 'users', 'everyone']]]
    roles: NotRequired[List[Snowflake]]
    users: NotRequired[List[Snowflake]]
    replied_user: NotRequired[bool]


# https://discord.com/developers/docs/resources/channel#role-subscription-data-object-role-subscription-data-object-structure


@final
class RoleSubscriptionData(TypedDict):
    role_subscription_listing_id: Snowflake
    tier_name: str
    total_months_subscribed: int
    is_renewal: bool


# https://discord.com/developers/docs/resources/channel#list-public-archived-threads-response-body


@final
class HasMoreListThreadsData(TypedDict):
    threads: List[ThreadChannelData]
    members: List[ThreadMemberData]
    has_more: bool
