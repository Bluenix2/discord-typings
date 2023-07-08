"""Python typings of all payloads that Discord sends as `TypedDict`s."""

# This file is not sorted by isort, but try to order the imports by
# name. The reason for this is because of circular imports in
# subclassing forcing imports to be in a certain order

# User needs to be imported before channel, due to UserMentionData subclass
from ._resources._user import *

from ._interactions._commands import *
from ._interactions._components import *
from ._interactions._receiving import *
from ._oauth import *
from ._reference import *
from ._resources._application import *
from ._resources._audit_log import *
from ._resources._auto_moderation import *
from ._resources._channel import *
from ._resources._emoji import *
from ._resources._guild import *
from ._resources._guild_scheduled_events import *
from ._resources._guild_template import *
from ._resources._invite import *
from ._resources._role_connection_metadata import *
from ._resources._stage_instance import *
from ._resources._sticker import *
from ._resources._voice import *
from ._resources._webhook import *

# Gateway imports several other things, so it is imported last
from ._gateway import *
