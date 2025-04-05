from typing import Dict, List, Optional

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'ApplicationData',
    'ApplicationIntegrationTypes',
    'ApplicationIntegrationTypeConfigurationData',
    'ApplicationEventWebhookStatus',
    'InstallParams',
    'ActivityInstanceData',
    'ActivityLocationData',
    'ActivityLocationKindEnum',
    'TeamMemberRoleTypes',
    'TeamData',
    'TeamMemberData',
)


# https://discord.com/developers/docs/resources/application#application-object-application-structure


class ApplicationData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    icon: Optional[str]
    description: str
    rpc_origins: NotRequired[List[str]]
    bot_public: bool
    bot_require_code_grant: bool
    bot: NotRequired['discord_typings.UserData']
    terms_of_service_url: NotRequired[str]
    privacy_policy_url: NotRequired[str]
    owner: NotRequired['discord_typings.UserData']
    verify_key: str
    team: Optional['discord_typings.TeamData']
    guild_id: NotRequired['discord_typings.Snowflake']
    guild: NotRequired['discord_typings.PartialGuildData']
    primary_sku_id: NotRequired['discord_typings.Snowflake']
    slug: NotRequired[str]
    cover_image: NotRequired[str]
    flags: NotRequired[int]
    approximate_guild_count: NotRequired[int]
    approximate_user_install_count: NotRequired[int]
    redirect_uris: NotRequired[List[str]]
    interactions_endpoint_url: NotRequired[Optional[str]]
    role_connections_verification_url: NotRequired[Optional[str]]
    event_webhooks_url: NotRequired[Optional[str]]
    event_webhooks_status: 'discord_typings.ApplicationEventWebhookStatus'
    event_webhooks_types: NotRequired[List[str]]
    tags: NotRequired[List[str]]
    install_params: NotRequired['discord_typings.InstallParams']
    integration_types_config: Dict[
        'discord_typings.ApplicationIntegrationTypes',
        'discord_typings.ApplicationIntegrationTypeConfigurationData'
    ]
    custom_install_url: NotRequired[str]


# https://discord.com/developers/docs/resources/application#application-object-application-integration-types


ApplicationIntegrationTypes = Literal[
    0,
    1,
]


# https://discord.com/developers/docs/resources/application#application-object-application-integration-type-configuration-object


class ApplicationIntegrationTypeConfigurationData(TypedDict):
    oauth2_install_params: 'discord_typings.InstallParams'


# https://discord.com/developers/docs/resources/application#application-object-application-event-webhook-status


ApplicationEventWebhookStatus = Literal[
    1,
    2,
    3,
]


# https://discord.com/developers/docs/resources/application#install-params-object-install-params-structure


class InstallParams(TypedDict):
    scopes: List['discord_typings.OAuth2Scopes']
    permissions: str


# https://discord.com/developers/docs/resources/application#get-application-activity-instance-activity-instance-object


class ActivityInstanceData(TypedDict):
    application_id: 'discord_typings.Snowflake'
    instance_id: str
    launch_id: 'discord_typings.Snowflake'
    location: 'discord_typings.ActivityLocationData'
    users: List['discord_typings.Snowflake']


# https://discord.com/developers/docs/resources/application#get-application-activity-instance-activity-location-object


class ActivityLocationData(TypedDict):
    id: str
    kind: 'discord_typings.ActivityLocationKindEnum'
    channel_id: 'discord_typings.Snowflake'
    guild_id: NotRequired[Optional['discord_typings.Snowflake']]


# https://discord.com/developers/docs/resources/application#get-application-activity-instance-activity-location-kind-enum


ActivityLocationKindEnum = Literal['gc', 'pc']


# https://discord.com/developers/docs/topics/teams#team-member-roles


TeamMemberRoleTypes = Literal['', 'admin', 'developer', 'read_only']


# https://discord.com/developers/docs/topics/teams#data-models-team-object


class TeamData(TypedDict):
    icon: Optional[str]
    id: 'discord_typings.Snowflake'
    members: List['discord_typings.TeamMemberData']
    name: str
    owner_user_id: 'discord_typings.Snowflake'


# https://discord.com/developers/docs/topics/teams#data-models-team-member-object


class TeamMemberData(TypedDict):
    membership_state: int
    team_id: 'discord_typings.Snowflake'
    user: 'discord_typings.UserData'
    role: str
