from typing import List, Optional, Union

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'PartialGuildData',
    'GuildData',
    'DefaultMessageNotificationLevels',
    'ExplicitContentFilterLevels',
    'MFALevels',
    'VerificationLevels',
    'GuildNSFWLevels',
    'PremiumTiers',
    'GuildFeatures',
    'UnavailableGuildData',
    'GuildPreviewData',
    'GuildWidgetSettingsData',
    'GuildWidgetData',
    'GuildMemberData',
    'StreamingIntegrationData',
    'DiscordIntegrationData',
    'IntegrationData',
    'IntegrationExpireBehaviors',
    'IntegrationAccountData',
    'IntegrationApplicationData',
    'BanData',
    'WelcomeScreenData',
    'WelcomeChannelData',
    'GuildOnboardingData',
    'GuildOnboardingPromptsData',
    'GuildOnboardingPromptOptionData',
    'GuildOnboardingModes',
    'GuildOnboardingPromptTypes',
    'ChannelPositionData',
    'ListThreadsData',
    'RolePositionData',
    'RoleData',
    'RoleTagsData',
    'PartialGuildData',
)


# https://discord.com/developers/docs/resources/user#get-current-user-guilds


class PartialGuildData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    icon: Optional[str]
    owner: bool
    permissions: str
    features: List['discord_typings.GuildFeatures']
    approximate_member_count: NotRequired[int]
    approximate_presence_count: NotRequired[int]


# https://discord.com/developers/docs/resources/guild#guild-object


class GuildData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    icon: Optional[str]
    icon_hash: NotRequired[Optional[str]]
    splash: Optional[str]
    discovery_splash: Optional[str]
    owner: NotRequired[bool]
    owner_id: 'discord_typings.Snowflake'
    permissions: NotRequired[str]
    afk_channel_id: Optional['discord_typings.Snowflake']
    afk_timeout: int
    widget_enabled: NotRequired[bool]
    widget_channel_id: NotRequired[Optional['discord_typings.Snowflake']]
    verification_level: 'discord_typings.VerificationLevels'
    default_message_notifications: 'discord_typings.DefaultMessageNotificationLevels'
    explicit_content_filter: 'discord_typings.ExplicitContentFilterLevels'
    roles: List['discord_typings.RoleData']
    emojis: List['discord_typings.EmojiData']
    features: List['discord_typings.GuildFeatures']
    mfa_level: 'discord_typings.MFALevels'
    application_id: Optional[str]
    system_channel_id: Optional['discord_typings.Snowflake']
    system_channel_flags: int
    rules_channel_id: Optional['discord_typings.Snowflake']
    max_presences: NotRequired[Optional[int]]
    max_members: NotRequired[int]
    vanity_url_code: Optional[str]
    description: Optional[str]
    banner: Optional[str]
    premium_tier: 'discord_typings.PremiumTiers'
    premium_subscription_count: NotRequired[int]
    preferred_locale: 'discord_typings.Locales'
    public_updates_channel_id: Optional['discord_typings.Snowflake']
    max_video_channel_users: NotRequired[int]
    max_stage_video_channel_users: NotRequired[int]
    approximate_member_count: NotRequired[int]
    approximate_presence_count: NotRequired[int]
    welcome_screen: NotRequired['discord_typings.WelcomeScreenData']
    nsfw_level: 'discord_typings.GuildNSFWLevels'
    stickers: NotRequired[List['discord_typings.StickerData']]
    premium_progress_bar_enabled: bool
    safety_alerts_channel_id: Optional['discord_typings.Snowflake']


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


GuildFeatures = Literal[
    'ANIMATED_BANNER',
    'ANIMATED_ICON',
    'APPLICATION_COMMAND_PERMISSIONS_V2',
    'AUTO_MODERATION',
    'BANNER',
    'COMMUNITY',
    'CREATOR_MONETIZABLE_PROVISIONAL',
    'CREATOR_STORE_PAGE',
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
    'RAID_ALERTS_DISABLED',
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


class UnavailableGuildData(TypedDict):
    id: str
    unavailable: bool


# https://discord.com/developers/docs/resources/guild#guild-preview-object-guild-preview-structure


class GuildPreviewData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    icon: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    emojis: List['discord_typings.EmojiData']
    features: List['discord_typings.GuildFeatures']
    approximate_member_count: int
    approximate_presence_count: int
    description: Optional[str]
    stickers: List['discord_typings.StickerData']


# https://discord.com/developers/docs/resources/guild#guild-widget-object-guild-widget-structure


class GuildWidgetSettingsData(TypedDict):
    enabled: bool
    channel_id: Optional['discord_typings.Snowflake']


# https://discord.com/developers/docs/resources/guild#guild-widget-object


class GuildWidgetData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    instant_invite: Optional[str]
    channels: List['discord_typings.PartialChannelData']
    members: List['discord_typings.UserData']
    presence_count: int


# https://discord.com/developers/docs/resources/guild#guild-member-object-guild-member-structure


class GuildMemberData(TypedDict):
    user: NotRequired['discord_typings.UserData']
    nick: NotRequired[Optional[str]]
    avatar: NotRequired[Optional[str]]
    roles: List['discord_typings.Snowflake']
    joined_at: str
    premium_since: NotRequired[Optional[str]]
    deaf: bool
    mute: bool
    flags: int
    pending: NotRequired[bool]
    permissions: NotRequired[str]
    communication_disabled_until: NotRequired[Optional[str]]


# https://discord.com/developers/docs/resources/guild#integration-object-integration-structure


class StreamingIntegrationData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    type: Literal['twitch', 'youtube', 'discord']
    enabled: bool
    syncing: bool
    role_id: NotRequired['discord_typings.Snowflake']
    enable_emoticons: bool
    expire_behavior: 'discord_typings.IntegrationExpireBehaviors'
    expire_grace_period: int
    user: NotRequired['discord_typings.UserData']
    account: 'discord_typings.IntegrationAccountData'
    synced_at: str
    subscriber_count: int
    revoked: bool
    application: 'discord_typings.IntegrationApplicationData'
    scopes: NotRequired[List['discord_typings.OAuth2Scopes']]


class DiscordIntegrationData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    type: Literal['discord']
    enabled: bool
    user: NotRequired['discord_typings.UserData']
    account: 'discord_typings.IntegrationAccountData'
    application: NotRequired['discord_typings.IntegrationApplicationData']
    scopes: NotRequired[List['discord_typings.OAuth2Scopes']]


IntegrationData = Union[StreamingIntegrationData, DiscordIntegrationData]


# https://discord.com/developers/docs/resources/guild#integration-object-integration-expire-behaviors


IntegrationExpireBehaviors = Literal[0, 1]


# https://discord.com/developers/docs/resources/guild#integration-account-object-integration-account-structure


class IntegrationAccountData(TypedDict):
    id: str
    name: str


# https://discord.com/developers/docs/resources/guild#integration-application-object-integration-application-structure


class IntegrationApplicationData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    icon: Optional[str]
    description: str
    summary: str
    bot: NotRequired[Optional['discord_typings.UserData']]


# https://discord.com/developers/docs/resources/guild#ban-object-ban-structure


class BanData(TypedDict):
    reason: Optional[str]
    user: 'discord_typings.UserData'


# https://discord.com/developers/docs/resources/guild#welcome-screen-object-welcome-screen-structure


class WelcomeScreenData(TypedDict):
    description: Optional[str]
    welcome_channels: List['discord_typings.WelcomeChannelData']


# https://discord.com/developers/docs/resources/guild#welcome-screen-object-welcome-screen-channel-structure


class WelcomeChannelData(TypedDict):
    channel_id: 'discord_typings.Snowflake'
    description: str
    emoji_id: Optional['discord_typings.Snowflake']
    emoji_name: Optional[str]


# https://discord.com/developers/docs/resources/guild#guild-onboarding-object


class GuildOnboardingData(TypedDict):
    guild_id: 'discord_typings.Snowflake'
    prompts: List['discord_typings.GuildOnboardingPromptsData']
    default_channel_ids: List['discord_typings.Snowflake']
    enabled: bool
    mode: 'discord_typings.GuildOnboardingModes'


# https://discord.com/developers/docs/resources/guild#guild-onboarding-object-onboarding-prompt-structure


class GuildOnboardingPromptsData(TypedDict):
    id: 'discord_typings.Snowflake'
    type: 'discord_typings.GuildOnboardingPromptTypes'
    options: List['discord_typings.GuildOnboardingPromptOptionData']
    title: str
    single_select: bool
    required: bool
    in_onboarding: bool


# https://discord.com/developers/docs/resources/guild#guild-onboarding-object-prompt-option-structure


class GuildOnboardingPromptOptionData(TypedDict):
    id: 'discord_typings.Snowflake'
    channel_ids: List['discord_typings.Snowflake']
    role_ids: List['discord_typings.Snowflake']
    emoji: 'discord_typings.EmojiData'
    title: str
    description: Optional[str]


# https://discord.com/developers/docs/resources/guild#guild-onboarding-object-onboarding-mode


GuildOnboardingModes = Literal[0, 1]


# https://discord.com/developers/docs/resources/guild#guild-onboarding-object-prompt-types


GuildOnboardingPromptTypes = Literal[0, 1]


# https://discord.com/developers/docs/resources/guild#modify-guild-channel-positions-json-params


class ChannelPositionData(TypedDict):
    id: 'discord_typings.Snowflake'
    position: Optional[int]
    lock_permissions: Optional[bool]
    parent_id: Optional['discord_typings.Snowflake']


# https://discord.com/developers/docs/resources/guild#list-active-threads-response-body


class ListThreadsData(TypedDict):
    threads: List['discord_typings.ThreadChannelData']
    members: List['discord_typings.ThreadMemberData']


# https://discord.com/developers/docs/resources/guild#modify-guild-role-positions-json-params


class RolePositionData(TypedDict):
    id: 'discord_typings.Snowflake'
    position: NotRequired[Optional[int]]


# https://discord.com/developers/docs/topics/permissions#role-object-role-structure


class RoleData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    color: int
    hoist: bool
    icon: NotRequired[Optional[str]]
    unicode_emoji: NotRequired[Optional[str]]
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    tags: NotRequired['discord_typings.RoleTagsData']
    flags: int


# https://discord.com/developers/docs/topics/permissions#role-object-role-tags-structure


class RoleTagsData(TypedDict):
    bot_id: NotRequired['discord_typings.Snowflake']
    integration_id: NotRequired['discord_typings.Snowflake']
    premium_subscriber: NotRequired[None]
    subscription_listing_id: NotRequired['discord_typings.Snowflake']
    available_for_purchase: NotRequired[None]
    guild_connections: NotRequired[None]
