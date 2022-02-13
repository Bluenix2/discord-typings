# discord-typings

Maintained typings of all payloads that Discord sends as `TypedDict`s.

## Naming and usage

Right now there is no official documentation or API Reference - just start
importing things and your editor will auto-complete options. This may change in
the future though.

The naming used is the suffixes `Data`, `Event` and `Command` for the three
types of payloads. `Event` refers to a gateway event received over the gateway,
`Command` refers to a gateway command sent over the gateway and `Data` is used
for any general top-level payloads like `UserData`.

The benefit of using `Data` as a suffix is that in your code you can use
`from discord_typings import UserData` even if you define a `User` object (as
is expected to be rather common).

### Exceptions

To differentiate between the data for complete application commands, and the
data Discord expects to receive to create an application command, there is
a special-cased `ApplicationCommandPayload`.
