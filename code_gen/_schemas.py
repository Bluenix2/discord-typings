import re
from typing import Any, Optional

from ._base import TypingGenerator
from ._config import IGNORE_SCHEMAS, PKG_NAME

__all__ = (
    'SchemaGenerator',
)

PREFIX = '\n'.join([
    'from typing import Any, Literal, Union',
    '',
    'from typing_extensions import NotRequired, TypedDict',
    '',
    f'import {PKG_NAME}',
    '',
    '# THIS FILE HAS BEEN GENERATED AUTOMATICALLY FROM THE OFFICIAL DISCORD',
    '# OPENAPI SPECIFICATION. REFER TO PROJECT DOCUMENTATION ON HOW TO RUN.',
    '# DO NOT EDIT MANUALLY.',
])


def _indent(line: str) -> str:
    return '    ' + line


class SchemaGenerator(TypingGenerator):
    _schemas: dict[str, list[str]]
    """A dictionary of schemas, represented as a dictionary of name to lines of code."""

    _current_schema: Optional[str]
    """Current top-level schema being generated / parsed."""

    _current_field: list[str]
    """Current field being processed, represented as a stack."""

    __slots__ = (
        '_schemas',
        '_current_schema',
        '_current_field',
    )

    _PRIMITIVE_TYPES = {
        'string': 'str',
        'integer': 'int',
        'number': 'float',
        'boolean': 'bool',
        'null': 'None',
    }
    _VALID_REF = re.compile(r'[a-zA-Z]+')
    _INVALID_KEYWORD = {
        'and',
        'as',
        'assert',
        'async',
        'await',
        # 'case',  # Implemented as a soft keyword
        'class',
        'def',
        'del',
        'elif',
        'else',
        'except',
        'finally',
        'for',
        'from',
        'global',
        'if',
        'in',
        'is',
        'lambda',
        # 'match',  # Implemented as a soft keyword
        'nonlocal',
        'not',
        'or',
        'raise',
        'return',
        'try',
        'while',
        'yield',
        'False',
        'None',
        'True',
    }

    def __init__(self) -> None:
        self._schemas = {}

        self._current_schema = None
        self._current_field = []

    def _generate_inline(self, annotation: dict[str, Any]) -> str:
        assert self._current_schema is not None

        field_suffix = ''.join([field.title() for field in self._current_field])
        schema_name = self._current_schema + field_suffix

        generated = self._generate_schema(schema_name, annotation)
        if not generated:
            raise ValueError(
                f'Sub-schema {repr(schema_name)} not generated: {repr(annotation)}'
            )

        return f"'{PKG_NAME}.API{schema_name}'"

    def _generate_fields(self, properties: dict[str, Any], required: list[str]) -> list[str]:
        required_lookup: frozenset[str] = frozenset(required)
        lines: list[str] = []

        for name, value in properties.items():
            self._current_field.append(name)

            annotation = self._parse_annotation(value)

            if name not in required_lookup:
                annotation = f'NotRequired[{annotation}]'

            lines.append(f'{name}: {annotation}')

            self._current_field.pop()

        return lines

    def _generate_schema(self, name: str, spec: dict[str, Any]) -> bool:
        if name in IGNORE_SCHEMAS:
            return False

        _old_schema = self._current_schema
        self._current_schema = name

        schema: list[str] = []

        if 'type' not in spec:
            print(f'No type; ignoring {repr(name)}: {repr(spec)}')
            self._current_schema = _old_schema
            return False

        # A "types" or "status" enum
        if spec['type'] in {'integer', 'string'}:
            if 'oneOf' not in spec:
                # Non-enum integer or string, this is used for Discord's own
                # custom types. For example Snowflake and Int53Type
                print(f'Non-enum primitive type; ignoring {repr(name)}: {repr(spec)}')
                self._current_schema = _old_schema
                return False

            values: list[str] = []
            for val in spec['oneOf']:
                values.append(repr(val['const']))

            schema.append(f'API{name} = Literal[')
            for val in values:
                schema.append(_indent(val + ','))
            schema.append(']')

        elif spec['type'] == 'object':
            if 'properties' not in spec:
                # Currently only used by the errors objects
                print(f'Object without properties; ignoring {repr(name)}: {repr(spec)}')
                self._current_schema = _old_schema
                return False

            schema.append(f'class API{name}(TypedDict):')

            if spec['properties']:
                schema.extend(
                    [
                        _indent(line) for line in
                        self._generate_fields(spec['properties'], spec.get('required', []))
                    ]
                )
            else:
                schema.append(_indent('pass'))

        else:
            raise NotImplementedError(f'Unknown schema {repr(name)}: {repr(spec)}')

        self._schemas[f'API{name}'] = schema

        self._current_schema = _old_schema
        return True

    def generate(self, spec: dict[str, Any]) -> str:
        for name, settings in spec['components']['schemas'].items():
            self._generate_schema(name, settings)

        symbols = [_indent(repr(symbol) + ',') for symbol in self._schemas]
        all_ = f"__all__: tuple[str, ...] = (\n{'\n'.join(symbols)}\n)"

        schemas = ['\n'.join(lines) for lines in self._schemas.values()]

        return (
            PREFIX +
            '\n\n' +
            all_ +
            '\n\n\n' +
            '\n\n\n'.join(schemas) +
            '\n'
        )
