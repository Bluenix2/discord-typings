PKG_NAME = 'discord_typings'

SCHEMA_FILE = 'discord_typings/_models.py'

IGNORE_SCHEMAS = {
    # Not implemented, typed as ints
    'Int53Type',
    'UInt32Type',

    # Implemented manually
    'SnowflakeType',

    # Special-cased manually
    'Error',
    'InnerErrors',
    'ErrorDetails',
    'ErrorResponse'
}

