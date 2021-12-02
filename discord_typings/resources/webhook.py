from typing import Optional

from typing_extensions import Literal, NotRequired, TypedDict

from ..shared import Snowflake
from .channel import PartialChannelData
from .guild import GuildData
from .user import UserData

__all__ = ('WebhookData',)


class WebhookData(TypedDict):
    id: Snowflake
    type: Literal[1, 2, 3]
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
