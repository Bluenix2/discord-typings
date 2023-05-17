# discord-typings

Python typings of all payloads that Discord sends as `TypedDict`s.

## Quickstart

The library requires no setup except for installation. The easiest way to
install it is through PyPI where it is similarly named `discord-typings`:

```bash
pip install discord-typings
```

Now, start importing the relevant typings directly from the library:

```python
from discord_typings import UserData


def print_author(user: UserData) -> None:
    print(f"Created by {user['username']}#{user['discriminator']}")


print_author({
    'id': '344404945359077377',
    'username': 'Bluenix',
    'discriminator': '7543',
    'avatar': None
})
```

It is also possible to import the library inside of a `TYPE_CHECKING`-clause:

```python
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from discord_typings import Snowflake


class Data:
    id: 'Snowflake'
    value: Any
```

> **Note**
> It is not recommended to import the library this way, as it does not allow
> you to introspect the annotations in other code. It is merely pointed out
> for completeness.

## Naming and Usage

There is no documentation or API reference as this provides no value on top of
the Discord developer documentation the types are based on. Typings are named
after the object they represent, and there are little to no
[exceptions](#exceptions) to this rule.

Typings use suffixes to differentiate between potential wrapping objects in
user code - such as importing `UserData` to parse into a custom `User` class.
These are `Data`, `Event`, and `Command`. `Event` refers to a gateway event
*received* over the gateway while `Command` refers to a gateway command *sent*
over the gateway. `Data` is used for any general objects like `UserData`.

### Exceptions

To differentiate between the data for complete application commands, and the
data Discord expects to receive to create an application command, there is
a special-cased `ApplicationCommandPayload`.

## Codestyle and Contributing

Discord-typings is a relatively simple library with little code, but
unfortunately needs to be constantly maintained with Discord's API.
The purpose of this library is for this to be a community effort;
any help with maintenance is greatly appreciated.

### Structure

The library follows the API docs both in terms of naming, structure, and order
inside of individual files. This should hopefully make it easier to find the
code to change when you have the documentation entry at hand.

All internal imports should be done by importing the entire module, then
accessing the typing as an attribute. If `from ... import ...`, or specific
things are imported, that is likely to create complicated circular imports.
Inside of annotations, wrap the attribute access (`discord_typings.X`) in
quotes to make it a string and defer its evaluation.

All typings which directly represent a Discord payload (excluding typings
created for the purpose of a `Union`) should be added to the file's `__all__`,
then be added to the module's `__init__` and its `__all__`.
