from typing import Union

# Somewhat useless but good to distinguish the difference, perhaps in the
# future Python's typing system will have something similar to TypeScript's
# "Template Literal Types" which is able to describe a snowflake.
# Discord handles integers on endpoints but all snowflakes received by the API
# will be strings.
# https://discord.com/developers/docs/reference#snowflakes
Snowflake = Union[str, int]
