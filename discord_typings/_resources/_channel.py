from typing import List, Optional, Union

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'PartialChannelData',
    'TextChannelData',
    'NewsChannelData',
    'DMChannelData',
    'GroupDMChannelData',
    'ThreadChannelData',
    'VoiceChannelData',
    'CategoryChannelData',
    'ForumChannelData',
    'MediaChannelData',
    'ChannelData',
    'ChannelTypes',
    'VideoQualityModes',
    'SortOrderTypes',
    'ForumLayoutTypes',
    'MessageData',
    'UserMentionData',
    'MessageTypes',
    'MessageActivityData',
    'MessageActivityTypes',
    'MessageReferenceData',
    'FollowedChannelData',
    'MessageReactionData',
    'ReactionCountDetailsData',
    'PermissionOverwriteData',
    'ThreadMetadataData',
    'ThreadMemberData',
    'DefaultReactionData',
    'ForumTagData',
    'EmbedData',
    'EmbedThumbnailData',
    'EmbedVideoData',
    'EmbedImageData',
    'EmbedProviderData',
    'EmbedAuthorData',
    'EmbedFooterData',
    'EmbedFieldData',
    'PartialAttachmentData',
    'AttachmentData',
    'ChannelMentionData',
    'AllowedMentionsData',
    'RoleSubscriptionData',
    'HasMoreListThreadsData',
)


# https://discord.com/developers/docs/resources/channel#channel-object-channel-structure


class PartialChannelData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    type: Literal[0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16]
    permissions: NotRequired[str]


class TextChannelData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: Literal[0]
    guild_id: NotRequired['discord_typings.Snowflake']
    position: int
    permission_overwrites: List['discord_typings.PermissionOverwriteData']
    name: str
    topic: Optional[str]
    nsfw: bool
    last_message_id: Optional['discord_typings.Snowflake']
    rate_limit_per_user: int
    parent_id: Optional['discord_typings.Snowflake']
    last_pin_timestamp: NotRequired[Optional[str]]
    default_auto_archive_duration: NotRequired[int]
    flags: int


class NewsChannelData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: Literal[5]
    guild_id: NotRequired['discord_typings.Snowflake']
    position: int
    permission_overwrites: List['discord_typings.PermissionOverwriteData']
    name: str
    topic: Optional[str]
    nsfw: bool
    last_message_id: Optional['discord_typings.Snowflake']
    parent_id: Optional['discord_typings.Snowflake']
    last_pin_timestamp: NotRequired[Optional[str]]
    default_auto_archive_duration: NotRequired[int]
    flags: int


class DMChannelData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: Literal[1]
    last_message_id: Optional['discord_typings.Snowflake']
    recipients: List['discord_typings.UserData']
    last_pin_timestamp: NotRequired[Optional[str]]
    flags: int


class GroupDMChannelData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: Literal[3]
    name: str
    last_message_id: Optional['discord_typings.Snowflake']
    recipients: List['discord_typings.UserData']
    icon: Optional[str]
    owner_id: 'discord_typings.Snowflake'
    application_id: NotRequired['discord_typings.Snowflake']
    managed: bool
    last_pin_timestamp: NotRequired[Optional[str]]
    flags: int


class ThreadChannelData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: Literal[10, 11, 12]
    guild_id: NotRequired['discord_typings.Snowflake']
    name: str
    last_message_id: Optional['discord_typings.Snowflake']
    rate_limit_per_user: int
    owner_id: 'discord_typings.Snowflake'
    parent_id: Optional['discord_typings.Snowflake']
    last_pin_timestamp: NotRequired[Optional[str]]
    message_count: int
    member_count: int
    thread_metadata: 'discord_typings.ThreadMetadataData'
    member: NotRequired['discord_typings.ThreadMemberData']
    flags: int
    total_messages_sent: int
    applied_tags: NotRequired[List['discord_typings.Snowflake']]


class VoiceChannelData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: Literal[2, 13]
    guild_id: NotRequired['discord_typings.Snowflake']
    position: int
    permission_overwrites: List['discord_typings.PermissionOverwriteData']
    name: str
    nsfw: bool
    last_message_id: NotRequired[Optional['discord_typings.Snowflake']]
    bitrate: int
    user_limit: int
    parent_id: Optional['discord_typings.Snowflake']
    last_pin_timestamp: NotRequired[Optional[str]]
    rtc_region: Optional[str]
    video_quality_mode: NotRequired['discord_typings.VideoQualityModes']
    flags: int


class CategoryChannelData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: Literal[4]
    guild_id: NotRequired['discord_typings.Snowflake']
    position: int
    permission_overwrites: List['discord_typings.PermissionOverwriteData']
    name: str
    nsfw: bool
    flags: int


class ForumChannelData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: Literal[15]
    guild_id: NotRequired['discord_typings.Snowflake']
    position: int
    permission_overwrites: List['discord_typings.PermissionOverwriteData']
    name: str
    topic: Optional[str]
    nsfw: bool
    last_message_id: Optional['discord_typings.Snowflake']
    rate_limit_per_user: int
    default_auto_archive_duration: NotRequired[int]
    flags: int
    available_tags: List['discord_typings.ForumTagData']
    default_reaction_emoji: Optional['discord_typings.DefaultReactionData']
    default_thread_rate_limit_per_user: int
    default_sort_order: Optional['discord_typings.SortOrderTypes']
    default_forum_layout: 'discord_typings.ForumLayoutTypes'


class MediaChannelData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: Literal[16]
    guild_id: NotRequired['discord_typings.Snowflake']
    position: int
    permission_overwrites: List['discord_typings.PermissionOverwriteData']
    name: str
    topic: Optional[str]
    nsfw: bool
    last_message_id: Optional['discord_typings.Snowflake']
    rate_limit_per_user: int
    default_auto_archive_duration: NotRequired[int]
    flags: int
    available_tags: List['discord_typings.ForumTagData']
    default_reaction_emoji: Optional['discord_typings.DefaultReactionData']
    default_thread_rate_limit_per_user: int
    default_sort_order: Optional['discord_typings.SortOrderTypes']
    default_forum_layout: 'discord_typings.ForumLayoutTypes'


ChannelData = Union[
    TextChannelData, NewsChannelData, DMChannelData, GroupDMChannelData,
    ThreadChannelData, VoiceChannelData, CategoryChannelData, ForumChannelData,
    MediaChannelData,
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


class _ChannelMessageData(TypedDict):
    id: 'discord_typings.Snowflake'
    channel_id: 'discord_typings.Snowflake'
    author: 'discord_typings.UserData'
    content: str
    timestamp: str
    edited_timestamp: Optional[str]
    tts: bool
    mention_everyone: bool
    mentions: Union[List['discord_typings.UserData'], List['discord_typings.UserMentionData']]
    mention_roles: List['discord_typings.Snowflake']
    mention_channels: NotRequired[List['discord_typings.ChannelMentionData']]
    attachments: List['discord_typings.AttachmentData']
    embeds: List['discord_typings.EmbedData']
    reactions: NotRequired[List['discord_typings.MessageReactionData']]
    nonce: NotRequired[Union[int, str]]
    pinned: bool
    webhook_id: NotRequired['discord_typings.Snowflake']
    type: 'discord_typings.MessageTypes'
    activity: NotRequired['discord_typings.MessageActivityData']
    application: NotRequired['discord_typings.ApplicationData']
    application_id: NotRequired['discord_typings.Snowflake']
    message_reference: NotRequired['discord_typings.MessageReferenceData']
    flags: NotRequired[int]
    referenced_message: NotRequired[Optional['discord_typings.MessageData']]
    interaction: NotRequired['discord_typings.MessageInteractionData']
    thread: NotRequired['discord_typings.ThreadChannelData']
    components: NotRequired[List['discord_typings.ComponentData']]
    sticker_items: NotRequired[List['discord_typings.StickerItemData']]
    position: NotRequired[int]
    role_subscription_data: NotRequired['discord_typings.RoleSubscriptionData']


class _GuildMessageData(_ChannelMessageData):
    guild_id: 'discord_typings.Snowflake'
    member: 'discord_typings.GuildMemberData'


MessageData = Union[_ChannelMessageData, _GuildMessageData]


class UserMentionData(discord_typings.UserData):
    member: 'discord_typings.GuildMemberData'


# https://discord.com/developers/docs/resources/channel#message-object-message-types


MessageTypes = Literal[
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
]


# https://discord.com/developers/docs/resources/channel#message-object-message-activity-structure


class MessageActivityData(TypedDict):
    type: 'discord_typings.MessageActivityTypes'
    party_id: NotRequired[str]


# https://discord.com/developers/docs/resources/channel#message-object-message-activity-types


MessageActivityTypes = Literal[1, 2, 3, 5]


# https://discord.com/developers/docs/resources/channel#message-reference-object-message-reference-structure


class MessageReferenceData(TypedDict):
    message_id: NotRequired['discord_typings.Snowflake']
    # Note: This will always be sent when receiving a message reference.
    channel_id: NotRequired['discord_typings.Snowflake']
    guild_id: NotRequired['discord_typings.Snowflake']
    fail_if_not_exists: NotRequired[bool]


# https://discord.com/developers/docs/resources/channel#followed-channel-object-followed-channel-structure


class FollowedChannelData(TypedDict):
    channel_id: 'discord_typings.Snowflake'
    webhook_id: 'discord_typings.Snowflake'


# https://discord.com/developers/docs/resources/channel#reaction-object-reaction-structure


class MessageReactionData(TypedDict):
    count: int
    count_details: 'discord_typings.ReactionCountDetailsData'
    me: bool
    me_burst: bool
    emoji: 'discord_typings.EmojiData'
    burst_colors: List[str]


# https://discord.com/developers/docs/resources/channel#reaction-count-details-object


class ReactionCountDetailsData(TypedDict):
    burst: int
    normal: int


# https://discord.com/developers/docs/resources/channel#overwrite-object-overwrite-structure


class PermissionOverwriteData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: Literal[0, 1]
    allow: str
    deny: str


# https://discord.com/developers/docs/resources/channel#thread-metadata-object-thread-metadata-structure


class ThreadMetadataData(TypedDict):
    archived: bool
    auto_archive_duration: int
    archive_timestamp: str
    locked: bool
    invitable: NotRequired[bool]
    create_timestamp: NotRequired[Optional[str]]


# https://discord.com/developers/docs/resources/channel#thread-member-object-thread-member-structure


class ThreadMemberData(TypedDict):
    id: NotRequired['discord_typings.Snowflake']
    user_id: NotRequired['discord_typings.Snowflake']
    member: NotRequired['discord_typings.GuildMemberData']
    join_timestamp: str
    flags: int


# https://discord.com/developers/docs/resources/channel#default-reaction-object-default-reaction-structure


class DefaultReactionData(TypedDict):
    emoji_name: Optional[str]
    emoji_id: Optional['discord_typings.Snowflake']


# https://discord.com/developers/docs/resources/channel#forum-tag-object-forum-tag-structure


class ForumTagData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    moderated: bool
    emoji_id: Optional['discord_typings.Snowflake']
    emoji_name: Optional['discord_typings.Snowflake']


# https://discord.com/developers/docs/resources/channel#embed-object-embed-structure


class EmbedData(TypedDict):
    title: NotRequired[str]
    type: NotRequired[Literal['rich', 'image', 'video', 'gifv', 'article', 'link']]
    description: NotRequired[str]
    url: NotRequired[str]
    timestamp: NotRequired[str]
    color: NotRequired[int]
    footer: NotRequired['discord_typings.EmbedFooterData']
    image: NotRequired['discord_typings.EmbedImageData']
    thumbnail: NotRequired['discord_typings.EmbedThumbnailData']
    video: NotRequired['discord_typings.EmbedVideoData']
    provider: NotRequired['discord_typings.EmbedProviderData']
    author: NotRequired['discord_typings.EmbedAuthorData']
    fields: NotRequired[List['discord_typings.EmbedFieldData']]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-thumbnail-structure


class EmbedThumbnailData(TypedDict):
    url: str
    proxy_url: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-video-structure


class EmbedVideoData(TypedDict):
    url: NotRequired[str]
    proxy_url: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-image-structure


class EmbedImageData(TypedDict):
    url: str
    proxy_url: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-provider-structure


class EmbedProviderData(TypedDict):
    name: NotRequired[str]
    url: NotRequired[str]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-author-structure


class EmbedAuthorData(TypedDict):
    name: str
    url: NotRequired[str]
    icon_url: NotRequired[str]
    proxy_icon_url: NotRequired[str]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-footer-structure


class EmbedFooterData(TypedDict):
    text: str
    icon_url: NotRequired[str]
    proxy_icon_url: NotRequired[str]


# https://discord.com/developers/docs/resources/channel#embed-object-embed-field-structure


class EmbedFieldData(TypedDict):
    name: str
    value: str
    inline: NotRequired[bool]


# https://discord.com/developers/docs/resources/channel#attachment-object-attachment-structure


class PartialAttachmentData(TypedDict):
    id: 'discord_typings.Snowflake'
    filename: NotRequired[str]
    description: NotRequired[str]


class AttachmentData(TypedDict):
    id: 'discord_typings.Snowflake'
    filename: str
    description: NotRequired[str]
    content_type: NotRequired[str]
    size: int
    url: str
    proxy_url: str
    height: NotRequired[Optional[int]]
    width: NotRequired[Optional[int]]
    ephemeral: NotRequired[bool]
    duration_secs: NotRequired[float]
    waveform: NotRequired[str]
    flags: NotRequired[int]


# https://discord.com/developers/docs/resources/channel#channel-mention-object-channel-mention-structure


class ChannelMentionData(TypedDict):
    id: 'discord_typings.Snowflake'
    guild_id: 'discord_typings.Snowflake'
    type: Literal[0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13]
    name: str


# https://discord.com/developers/docs/resources/channel#allowed-mentions-object-allowed-mentions-structure


class AllowedMentionsData(TypedDict):
    parse: NotRequired[List[Literal['roles', 'users', 'everyone']]]
    roles: NotRequired[List['discord_typings.Snowflake']]
    users: NotRequired[List['discord_typings.Snowflake']]
    replied_user: NotRequired[bool]


# https://discord.com/developers/docs/resources/channel#role-subscription-data-object-role-subscription-data-object-structure


class RoleSubscriptionData(TypedDict):
    role_subscription_listing_id: 'discord_typings.Snowflake'
    tier_name: str
    total_months_subscribed: int
    is_renewal: bool


# https://discord.com/developers/docs/resources/channel#list-public-archived-threads-response-body


class HasMoreListThreadsData(TypedDict):
    threads: List[ThreadChannelData]
    members: List[ThreadMemberData]
    has_more: bool
