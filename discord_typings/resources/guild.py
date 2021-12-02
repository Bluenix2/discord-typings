from __future__ import annotations

from typing import List, Optional

from typing_extensions import Literal, NotRequired, TypedDict

from ..shared import Snowflake
from .emoji import EmojiData
from .sticker import StickerData
from .user import UserData

__all__ = (
    'GuildData', 'GuildPreviewData', 'StreamingIntegrationData',
    'DiscordIntegrationData', 'IntegrationAccountData',
    'IntegrationApplicationData', 'BanData', 'WelcomeScreenData', 'RoleData'
)


class GuildData(TypedDict):
    id: str
    name: str
    icon: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    owner: NotRequired[bool]
    owner_id: str
    permissions: NotRequired[str]
    afk_channel_id: Optional[str]
    afk_timeout: int
    widget_enabled: NotRequired[bool]
    widget_channel_id: NotRequired[Optional[str]]
    verification_level: Literal[0, 1, 2, 3, 4]
    default_message_notifications: Literal[0, 1]
    explicit_content_filter: Literal[0, 1, 2]
    roles: List[RoleData]
    emojis: List[EmojiData]
    features: List[GuildFeatures]
    mfa_level: Literal[0, 1]
    application_id: Optional[str]
    system_channel_id: Optional[str]
    system_channel_flags: int
    rules_channel_id: Optional[str]
    max_presences: NotRequired[Optional[int]]
    max_members: NotRequired[int]
    vanity_url_code: Optional[str]
    description: Optional[str]
    banner: Optional[str]
    premium_tier: Literal[0, 1, 2, 3]
    premium_subscription_count: NotRequired[int]
    preferred_locale: str
    public_updates_channel_id: Optional[str]
    max_video_channel_users: NotRequired[int]
    approximate_member_count: NotRequired[int]
    approximate_presence_count: NotRequired[int]
    welcome_screen: NotRequired[WelcomeScreenData]
    nsfw_level: Literal[0, 1, 2, 3]
    stickers: List[StickerData]


GuildFeatures = Literal[
    'ANIMATED_ICON', 'BANNER', 'COMMERCE', 'COMMUNITY', 'DISCOVERABLE',
    'FEATUREABLE', 'INVITE_SPLASH', 'MEMBER_VERIFICATION_GATE_ENABLED',
    'MONETIZATION_ENABLED', 'MORE_STICKERS', 'NEWS', 'PARTNERED',
    'PREVIEW_ENABLED', 'PRIVATE_THREADS', 'ROLE_ICONS',
    'SEVEN_DAY_THREAD_ARCHIVE', 'THREE_DAY_THREAD_ARCHIVE',
    'TICKETED_EVENTS_ENABLED', 'VANITY_URL', 'VERIFIED',
    'VIP_REGIONS', 'WELCOME_SCREEN_ENABLED'
]


class GuildPreviewData(TypedDict):
    id: Snowflake
    name: str
    icon: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    emojis: List[EmojiData]
    features: List[GuildFeatures]
    approximate_member_count: int
    approximate_presence_count: int
    description: Optional[str]


class GuildWidgetData(TypedDict):
    enabled: bool
    channel_id: Optional[Snowflake]


class GuildMemberData(TypedDict):
    user: NotRequired[UserData]
    nick: NotRequired[Optional[str]]
    avatar: NotRequired[Optional[str]]
    roles: List[Snowflake]
    joined_at: str
    premium_since: NotRequired[Optional[str]]
    deaf: bool
    mute: bool
    pending: NotRequired[bool]
    permissions: NotRequired[str]


class StreamingIntegrationData(TypedDict):
    id: Snowflake
    name: str
    type: Literal['twitch', 'youtube', 'discord']
    enabled: bool
    syncing: bool
    role_id: NotRequired[Snowflake]
    enable_emoticons: bool
    expire_behavior: Literal[0, 1]
    expire_grace_period: int
    user: UserData
    account: IntegrationAccountData
    synced_at: str
    subscriber_count: int
    revoked: bool
    application: IntegrationApplicationData


class DiscordIntegrationData(TypedDict):
    id: Snowflake
    name: str
    type: Literal['discord']
    enabled: bool
    account: IntegrationAccountData
    application: NotRequired[IntegrationApplicationData]


class IntegrationAccountData(TypedDict):
    id: Snowflake
    name: str


class IntegrationApplicationData(TypedDict):
    id: Snowflake
    name: str
    icon: NotRequired[str]
    description: str
    summary: str
    bot: Optional[UserData]


class BanData(TypedDict):
    reason: Optional[str]
    user: UserData


class WelcomeScreenData(TypedDict):
    description: Optional[str]
    welcome_channels: List[WelcomeChannelData]


class WelcomeChannelData(TypedDict):
    channel_id: Snowflake
    description: str
    emoji_id: Optional[Snowflake]
    emoji_name: Optional[str]


class RoleData(TypedDict):
    id: Snowflake
    name: str
    color: int
    hoist: bool
    icon: NotRequired[Optional[str]]
    unicode_emoji: NotRequired[Optional[str]]
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    tags: NotRequired[RoleTagsData]


class RoleTagsData(TypedDict):
    bot_id: NotRequired[Snowflake]
    integration_id: NotRequired[Snowflake]
    premium_subscriber: NotRequired[None]
