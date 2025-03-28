# Contributing to discord-typings

## Code Generation

The code generation for discord-typings has been implemented manually, without
any separate library. This is because of the overall niche use-case and
the fact that the library needs to special-case things for the Discord API.

### Running the CLI

The code generation should be invoked from the root directory, using the `-m`
flag to Python, as follows:

```bash
python -m code_gen schema openapi.json
```

Where `openapi.json` is the name of the file to read for the schema. This will
by default replace the file specified in `code_gen/_config.py`.
