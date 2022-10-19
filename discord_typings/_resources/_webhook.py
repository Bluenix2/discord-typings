from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from typing_extensions import Literal, NotRequired, TypedDict, final

if TYPE_CHECKING:
    from .._reference import Snowflake
    from ._channel import PartialChannelData
    from ._guild import GuildData
    from ._user import UserData

__all__ = ('WebhookData', 'WebhookTypes')


# https://discord.com/developers/docs/resources/webhook#webhook-object-webhook-structure


@final
class WebhookData(TypedDict):
    id: Snowflake
    type: WebhookTypes
    guild_id: NotRequired[Optional[Snowflake]]
    channel_id: Optional[Snowflake]
    user: NotRequired[UserData]
    name: Optional[str]
    avatar: Optional[str]
    token: NotRequired[str]
    application_id: Optional[Snowflake]
    source_guild: NotRequired[GuildData]
    source_channel: NotRequired[PartialChannelData]
    url: NotRequired[str]


# https://discord.com/developers/docs/resources/webhook#webhook-object-webhook-types


WebhookTypes = Literal[1, 2, 3]
