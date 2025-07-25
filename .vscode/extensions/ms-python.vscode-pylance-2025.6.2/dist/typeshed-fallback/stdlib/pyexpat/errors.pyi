import sys
from typing import Final
from typing_extensions import LiteralString

codes: dict[str, int]
messages: dict[int, str]

XML_ERROR_ABORTED: Final[LiteralString]
XML_ERROR_ASYNC_ENTITY: Final[LiteralString]
XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF: Final[LiteralString]
XML_ERROR_BAD_CHAR_REF: Final[LiteralString]
XML_ERROR_BINARY_ENTITY_REF: Final[LiteralString]
XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING: Final[LiteralString]
XML_ERROR_DUPLICATE_ATTRIBUTE: Final[LiteralString]
XML_ERROR_ENTITY_DECLARED_IN_PE: Final[LiteralString]
XML_ERROR_EXTERNAL_ENTITY_HANDLING: Final[LiteralString]
XML_ERROR_FEATURE_REQUIRES_XML_DTD: Final[LiteralString]
XML_ERROR_FINISHED: Final[LiteralString]
XML_ERROR_INCOMPLETE_PE: Final[LiteralString]
XML_ERROR_INCORRECT_ENCODING: Final[LiteralString]
XML_ERROR_INVALID_TOKEN: Final[LiteralString]
XML_ERROR_JUNK_AFTER_DOC_ELEMENT: Final[LiteralString]
XML_ERROR_MISPLACED_XML_PI: Final[LiteralString]
XML_ERROR_NOT_STANDALONE: Final[LiteralString]
XML_ERROR_NOT_SUSPENDED: Final[LiteralString]
XML_ERROR_NO_ELEMENTS: Final[LiteralString]
XML_ERROR_NO_MEMORY: Final[LiteralString]
XML_ERROR_PARAM_ENTITY_REF: Final[LiteralString]
XML_ERROR_PARTIAL_CHAR: Final[LiteralString]
XML_ERROR_PUBLICID: Final[LiteralString]
XML_ERROR_RECURSIVE_ENTITY_REF: Final[LiteralString]
XML_ERROR_SUSPENDED: Final[LiteralString]
XML_ERROR_SUSPEND_PE: Final[LiteralString]
XML_ERROR_SYNTAX: Final[LiteralString]
XML_ERROR_TAG_MISMATCH: Final[LiteralString]
XML_ERROR_TEXT_DECL: Final[LiteralString]
XML_ERROR_UNBOUND_PREFIX: Final[LiteralString]
XML_ERROR_UNCLOSED_CDATA_SECTION: Final[LiteralString]
XML_ERROR_UNCLOSED_TOKEN: Final[LiteralString]
XML_ERROR_UNDECLARING_PREFIX: Final[LiteralString]
XML_ERROR_UNDEFINED_ENTITY: Final[LiteralString]
XML_ERROR_UNEXPECTED_STATE: Final[LiteralString]
XML_ERROR_UNKNOWN_ENCODING: Final[LiteralString]
XML_ERROR_XML_DECL: Final[LiteralString]
if sys.version_info >= (3, 11):
    XML_ERROR_RESERVED_PREFIX_XML: Final[LiteralString]
    XML_ERROR_RESERVED_PREFIX_XMLNS: Final[LiteralString]
    XML_ERROR_RESERVED_NAMESPACE_URI: Final[LiteralString]
    XML_ERROR_INVALID_ARGUMENT: Final[LiteralString]
    XML_ERROR_NO_BUFFER: Final[LiteralString]
    XML_ERROR_AMPLIFICATION_LIMIT_BREACH: Final[LiteralString]
if sys.version_info >= (3, 14):
    XML_ERROR_NOT_STARTED: Final[LiteralString]
