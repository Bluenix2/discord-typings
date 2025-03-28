import re
from typing import Any

from ._config import PKG_NAME

__all__ = (
    'TypingGenerator',
)


class TypingGenerator:
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

    def _verify_ref(self, ref: str) -> None:
        if not self._VALID_REF.match(ref):
            raise ValueError(f'Invalid reference {repr(ref)} (does not match [a-zA-Z]+)')

        if ref in self._INVALID_KEYWORD:
            raise ValueError(f'Invalid reference {repr(ref)} (invalid keyword)')

    def _parse_reference(self, ref: str) -> str:
        if not ref.startswith('#/components/schemas/'):
            raise ValueError(
                f"Reference does not start with expected '#/components/schemas/': {repr(ref)}"
            )

        schema = ref.removeprefix('#/components/schemas/')
        self._verify_ref(schema)

        if schema == 'SnowflakeType':
            # Special-case for snowflakes, remove 'Type'
            return f"'{PKG_NAME}.APISnowflake'"
        elif schema == 'Int53Type':
            # Discord's own weird int type, gets parse as normal
            # int in Python by the JSON module
            return 'int'
        elif schema == 'UInt32Type':
            return 'int'

        return f"'{PKG_NAME}.API{schema}'"

    def _parse_primitive(self, annotation: str) -> str:
        return self._PRIMITIVE_TYPES[annotation]

    def _parse_annotation(self, annotation: dict[str, Any]) -> str:
        if '$ref' in annotation:
            return self._parse_reference(annotation['$ref'])

        elif 'enum' in annotation:
            consts = [repr(val) for val in annotation['enum']]

            return f"Literal[{', '.join(consts)}]"

        # Unclear what the difference between oneOf and anyOf is in the
        # case of Discord's API
        elif 'oneOf' in annotation:
            union = [self._parse_annotation(field) for field in annotation['oneOf']]

            # No need to special-case for Optional, it's usually done by
            # type-checkers anyways
            # TODO: In Python 3.10, replace with the pipe operator
            return f"Union[{', '.join(union)}]"
        elif 'anyOf' in annotation:
            union = [self._parse_annotation(field) for field in annotation['anyOf']]

            return f"Union[{', '.join(union)}]"

        elif 'type' in annotation:
            if annotation['type'] == 'array':
                return f"list[{self._parse_annotation(annotation['items'])}]"

            elif annotation['type'] == 'object':
                if 'additionalProperties' in annotation:
                    # Untyped additional properties, have to default to a dict
                    value = self._parse_annotation(annotation['additionalProperties'])
                    return f'dict[str, {value}]'
                elif 'properties' in annotation:
                    # An inline sub-schema, instead of a reference. We have to
                    # automatically create a new schema. Hence, reoccur back
                    # to gen_schema.
                    return self._generate_inline(annotation)
                else:
                    raise NotImplementedError(
                        f"Unknown annotation for {self._current_schema}" +
                        f" ({'.'.join(self._current_field)}): {repr(annotation)}"
                    )

            elif isinstance(annotation['type'], list):
                # This is essentially a lazy union, because instead of a list of
                # annotations (objects) in the case of 'oneOf', 'type' is a list
                # of types where you have to grab their metadata from the parent
                union: list[str] = []
                for field_type in annotation['type']:
                    field_annotation = annotation.copy()
                    field_annotation['type'] = field_type
                    union.append(self._parse_annotation(field_annotation))

                return f"Union[{', '.join(union)}]"
            else:
                return self._parse_primitive(annotation['type'])

        elif len(annotation) == 0:
            # Empty object, for example in AuditLogObjectChangeResponse
            return 'Any'

        else:
            raise NotImplementedError(
                f"Unknown annotation for {self._current_schema}" +
                f" ({'.'.join(self._current_field)}): {repr(annotation)}"
            )

    def _generate_inline(self, annotation: dict[str, Any]) -> str:
        """Generate a typing for an inline schema.

        This method is designed to be overriden by subclasses to program how
        the class should create this typing for an inline schema.

        Returns:
            The valid annotation for the generated schema.
        """
        raise NotImplementedError()
