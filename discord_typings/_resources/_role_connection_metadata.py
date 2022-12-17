from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from .._reference import Locales

__all__ = (
    'ApplicationRoleConnectionMetadataData',
    'ApplicationRoleConnectionMetadataTypes',
)


# https://discord.com/developers/docs/resources/application-role-connection-metadata#application-role-connection-metadata-object


@final
class ApplicationRoleConnectionMetadataData(TypedDict):
    type: ApplicationRoleConnectionMetadataTypes
    key: str
    name: str
    name_localizations: NotRequired[Optional[Dict[Locales, str]]]
    description: str
    description_localizations: NotRequired[Optional[Dict[Locales, str]]]


# https://discord.com/developers/docs/resources/application-role-connection-metadata#application-role-connection-metadata-object-application-role-connection-metadata-type


ApplicationRoleConnectionMetadataTypes = Literal[1, 2, 3, 4, 5, 6, 7, 8]
