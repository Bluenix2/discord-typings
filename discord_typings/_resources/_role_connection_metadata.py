from typing import Dict, Optional

from typing_extensions import Literal, NotRequired, TypedDict

import discord_typings

__all__ = (
    'ApplicationRoleConnectionMetadataData',
    'ApplicationRoleConnectionMetadataTypes',
)


# https://discord.com/developers/docs/resources/application-role-connection-metadata#application-role-connection-metadata-object


class ApplicationRoleConnectionMetadataData(TypedDict):
    type: 'discord_typings.ApplicationRoleConnectionMetadataTypes'
    key: str
    name: str
    name_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict['discord_typings.Locales', str]]]


# https://discord.com/developers/docs/resources/application-role-connection-metadata#application-role-connection-metadata-object-application-role-connection-metadata-type


ApplicationRoleConnectionMetadataTypes = Literal[1, 2, 3, 4, 5, 6, 7, 8]
