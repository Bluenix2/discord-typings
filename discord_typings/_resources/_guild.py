from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from .._oauth import OAuth2Scopes
    from .._reference import Locales, Snowflake
    from ._channel import ChannelData, ThreadChannelData, ThreadMemberData
    from ._emoji import EmojiData
    from ._sticker import StickerData
    from ._user import UserData

__all__ = (
    'GuildData', 'DefaultMessageNotificationLevels', 'ExplicitContentFilterLevels',
    'MFALevels', 'VerificationLevels', 'GuildNSFWLevels', 'PremiumTiers', 'GuildFeaturesData',
    'UnavailableGuildData', 'GuildPreviewData', 'GuildWidgetSettingsData', 'GuildWidgetData',
    'GuildMemberData', 'StreamingIntegrationData', 'DiscordIntegrationData', 'IntegrationData',
    'IntegrationExpireBehaviors', 'IntegrationAccountData', 'IntegrationApplicationData',
    'BanData', 'WelcomeScreenData', 'WelcomeChannelData', 'ChannelPositionData',
    'ListThreadsData', 'RolePositionData', 'RoleData', 'RoleTagsData',
    'PartialGuildData'
)


# https://discord.com/developers/docs/resources/user#get-current-user-guilds


@final
class PartialGuildData(TypedDict):
    id: Snowflake
    name: str
    icon: Optional[str]
    owner: bool
    permissions: str
    features: List[GuildFeaturesData]


# https://discord.com/developers/docs/resources/guild#guild-object-guild-structure


@final
class GuildData(TypedDict):
    id: Snowflake
    name: str
    icon: Optional[str]
    icon_hash: NotRequired[Optional[str]]
    splash: Optional[str]
    discovery_splash: Optional[str]
    owner: NotRequired[bool]
    owner_id: Snowflake
    permissions: NotRequired[str]
    afk_channel_id: Optional[Snowflake]
    afk_timeout: int
    widget_enabled: NotRequired[bool]
    widget_channel_id: NotRequired[Optional[Snowflake]]
    verification_level: VerificationLevels
    default_message_notifications: DefaultMessageNotificationLevels
    explicit_content_filter: ExplicitContentFilterLevels
    roles: List[RoleData]
    emojis: List[EmojiData]
    features: List[GuildFeaturesData]
    mfa_level: MFALevels
    application_id: Optional[str]
    system_channel_id: Optional[Snowflake]
    system_channel_flags: int
    rules_channel_id: Optional[Snowflake]
    max_presences: NotRequired[Optional[int]]
    max_members: NotRequired[int]
    vanity_url_code: Optional[str]
    description: Optional[str]
    banner: Optional[str]
    premium_tier: PremiumTiers
    premium_subscription_count: NotRequired[int]
    preferred_locale: Locales
    public_updates_channel_id: Optional[Snowflake]
    max_video_channel_users: NotRequired[int]
    approximate_member_count: NotRequired[int]
    approximate_presence_count: NotRequired[int]
    welcome_screen: NotRequired[WelcomeScreenData]
    nsfw_level: GuildNSFWLevels
    stickers: NotRequired[List[StickerData]]
    premium_progress_bar_enabled: bool


# https://discord.com/developers/docs/resources/guild#guild-object-default-message-notification-level


DefaultMessageNotificationLevels = Literal[0, 1]


# https://discord.com/developers/docs/resources/guild#guild-object-explicit-content-filter-level


ExplicitContentFilterLevels = Literal[0, 1, 2]


# https://discord.com/developers/docs/resources/guild#guild-object-mfa-level


MFALevels = Literal[0, 1]


# https://discord.com/developers/docs/resources/guild#guild-object-verification-level


VerificationLevels = Literal[0, 1, 2, 3, 4]


# https://discord.com/developers/docs/resources/guild#guild-object-guild-nsfw-level


GuildNSFWLevels = Literal[0, 1, 2, 3]


# https://discord.com/developers/docs/resources/guild#guild-object-premium-tier


PremiumTiers = Literal[0, 1, 2, 3]


# https://discord.com/developers/docs/resources/guild#guild-object-guild-features


GuildFeaturesData = Literal[
    'ANIMATED_BANNER',
    'ANIMATED_ICON',
    'APPLICATION_COMMAND_PERMISSIONS_V2',
    'AUTO_MODERATION',
    'BANNER',
    'COMMUNITY',
    'DEVELOPER_SUPPORT_SERVER',
    'DISCOVERABLE',
    'FEATUREABLE',
    'INVITES_DISABLED',
    'INVITE_SPLASH',
    'MEMBER_VERIFICATION_GATE_ENABLED',
    'MORE_STICKERS',
    'NEWS',
    'PARTNERED',
    'PREVIEW_ENABLED',
    'ROLE_ICONS',
    'ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE',
    'ROLE_SUBSCRIPTIONS_ENABLED',
    'TICKETED_EVENTS_ENABLED',
    'VANITY_URL',
    'VERIFIED',
    'VIP_REGIONS',
    'WELCOME_SCREEN_ENABLED',
]


# https://discord.com/developers/docs/resources/guild#unavailable-guild-object-example-unavailable-guild


@final
class UnavailableGuildData(TypedDict):
    id: str
    unavailable: bool


# https://discord.com/developers/docs/resources/guild#guild-preview-object-guild-preview-structure


@final
class GuildPreviewData(TypedDict):
    id: Snowflake
    name: str
    icon: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    emojis: List[EmojiData]
    features: List[GuildFeaturesData]
    approximate_member_count: int
    approximate_presence_count: int
    description: Optional[str]
    stickers: List[StickerData]


# https://discord.com/developers/docs/resources/guild#guild-widget-object-guild-widget-structure


@final
class GuildWidgetSettingsData(TypedDict):
    enabled: bool
    channel_id: Optional[Snowflake]


# https://discord.com/developers/docs/resources/guild#get-guild-widget-object-get-guild-widget-structure


@final
class GuildWidgetData(TypedDict):
    id: Snowflake
    name: str
    instant_invite: Optional[str]
    channels: List[ChannelData]
    members: List[UserData]
    presence_count: int


# https://discord.com/developers/docs/resources/guild#guild-member-object-guild-member-structure


@final
class GuildMemberData(TypedDict):
    user: NotRequired[UserData]
    nick: NotRequired[Optional[str]]
    avatar: NotRequired[Optional[str]]
    roles: List[Snowflake]
    joined_at: str
    premium_since: NotRequired[Optional[str]]
    deaf: bool
    mute: bool
    flags: int
    pending: NotRequired[bool]
    permissions: NotRequired[str]
    communication_disabled_until: NotRequired[Optional[str]]


# https://discord.com/developers/docs/resources/guild#integration-object-integration-structure


@final
class StreamingIntegrationData(TypedDict):
    id: Snowflake
    name: str
    type: Literal['twitch', 'youtube', 'discord']
    enabled: bool
    syncing: bool
    role_id: NotRequired[Snowflake]
    enable_emoticons: bool
    expire_behavior: IntegrationExpireBehaviors
    expire_grace_period: int
    user: NotRequired[UserData]
    account: IntegrationAccountData
    synced_at: str
    subscriber_count: int
    revoked: bool
    application: IntegrationApplicationData
    scopes: NotRequired[List[OAuth2Scopes]]


@final
class DiscordIntegrationData(TypedDict):
    id: Snowflake
    name: str
    type: Literal['discord']
    enabled: bool
    user: NotRequired[UserData]
    account: IntegrationAccountData
    application: NotRequired[IntegrationApplicationData]
    scopes: NotRequired[List[OAuth2Scopes]]


IntegrationData = Union[StreamingIntegrationData, DiscordIntegrationData]


# https://discord.com/developers/docs/resources/guild#integration-object-integration-expire-behaviors


IntegrationExpireBehaviors = Literal[0, 1]


# https://discord.com/developers/docs/resources/guild#integration-account-object-integration-account-structure


@final
class IntegrationAccountData(TypedDict):
    id: str
    name: str


# https://discord.com/developers/docs/resources/guild#integration-application-object-integration-application-structure


@final
class IntegrationApplicationData(TypedDict):
    id: Snowflake
    name: str
    icon: Optional[str]
    description: str
    summary: str
    bot: NotRequired[Optional[UserData]]


# https://discord.com/developers/docs/resources/guild#ban-object-ban-structure


@final
class BanData(TypedDict):
    reason: Optional[str]
    user: UserData


# https://discord.com/developers/docs/resources/guild#welcome-screen-object-welcome-screen-structure


@final
class WelcomeScreenData(TypedDict):
    description: Optional[str]
    welcome_channels: List[WelcomeChannelData]


# https://discord.com/developers/docs/resources/guild#welcome-screen-object-welcome-screen-channel-structure


@final
class WelcomeChannelData(TypedDict):
    channel_id: Snowflake
    description: str
    emoji_id: Optional[Snowflake]
    emoji_name: Optional[str]


# https://discord.com/developers/docs/resources/guild#modify-guild-channel-positions-json-params


@final
class ChannelPositionData(TypedDict):
    id: Snowflake
    position: Optional[int]
    lock_permissions: Optional[bool]
    parent_id: Optional[Snowflake]


# https://discord.com/developers/docs/resources/guild#list-active-threads-response-body


@final
class ListThreadsData(TypedDict):
    threads: List[ThreadChannelData]
    members: List[ThreadMemberData]


# https://discord.com/developers/docs/resources/guild#modify-guild-role-positions-json-params


@final
class RolePositionData(TypedDict):
    id: Snowflake
    position: NotRequired[Optional[int]]


# https://discord.com/developers/docs/topics/permissions#role-object-role-structure


@final
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


# https://discord.com/developers/docs/topics/permissions#role-object-role-tags-structure


@final
class RoleTagsData(TypedDict):
    bot_id: NotRequired[Snowflake]
    integration_id: NotRequired[Snowflake]
    premium_subscriber: NotRequired[None]
    subscription_listing_id: NotRequired[Snowflake]
    available_for_purchase: NotRequired[None]
    guild_connections: NotRequired[None]
