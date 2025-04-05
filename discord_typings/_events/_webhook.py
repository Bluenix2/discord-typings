from typing import Any, Dict, Generic, List, Mapping, TypeVar

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import discord_typings

__all__ = (
    'WebhookEvent',
    'GenericWebhookEventBody',
    'WebhookTypes',
    'WebhookApplicationAuthorizedData',
    'WebhookApplicationAuthorizedEvent',
    'WebhookEntitlementCreateData',
    'WebhookEntitlementCreateEvent',
)


_D = TypeVar('_D', bound='Mapping[str, Any]')
_T = TypeVar('_T', bound='str')  # Literal


# https://discord.com/developers/docs/events/webhook-events#payload-structure


class WebhookEvent(TypedDict):
    version: int
    application_id: 'discord_typings.Snowflake'
    type: 'discord_typings.WebhookTypes'
    event: 'discord_typings.GenericWebhookEventBody[str, Dict[str, Any]]'


class GenericWebhookEventBody(TypedDict, Generic[_T, _D]):
    """Generic Webhook event body.

    Inspired by the similar implementation of GenericDispatchEvent for
    gateway events.

    This should be considered internal.
    """
    type: _T
    timestamp: str
    data: _D


# https://discord.com/developers/docs/events/webhook-events#webhook-types


WebhookTypes = Literal[0, 1]


# https://discord.com/developers/docs/events/webhook-events#application-authorized


class WebhookApplicationAuthorizedData(TypedDict):
    integration_type: NotRequired['discord_typings.ApplicationIntegrationTypes']
    user: 'discord_typings.UserData'
    scopes: List['discord_typings.OAuth2Scopes']
    guild: NotRequired['discord_typings.GuildData']


WebhookApplicationAuthorizedEvent = GenericWebhookEventBody[
    Literal['APPLICATION_AUTHORIZED'], WebhookApplicationAuthorizedData
]


# https://discord.com/developers/docs/events/webhook-events#entitlement-create


WebhookEntitlementCreateData: TypeAlias = 'discord_typings.EntitlementData'


WebhookEntitlementCreateEvent = GenericWebhookEventBody[
    Literal['ENTITLEMENT_CREATE'], WebhookEntitlementCreateData
]
