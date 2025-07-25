from _typeshed import SliceableBuffer, Unused
from collections.abc import Sequence
from typing import Any, Protocol, type_check_only
from typing_extensions import TypeAlias

_FourIntSequence: TypeAlias = Sequence[int]
_TwoIntSequence: TypeAlias = Sequence[int]

@type_check_only
class _Kid(Protocol):
    def toRaw(self) -> bytes: ...
    def __str__(self, indent: str = "", /) -> str: ...

# All the classes below are used in version_file_info generated by `pyi-grab_version`
# See: https://pyinstaller.org/en/stable/usage.html#capturing-windows-version-data

# VSVersionInfo is also by other types referenced in https://pyinstaller.org/en/stable/spec-files.html#spec-file-operation
class VSVersionInfo:
    ffi: FixedFileInfo | None
    kids: list[_Kid]
    def __init__(self, ffi: FixedFileInfo | None = None, kids: list[_Kid] | None = None) -> None: ...
    def fromRaw(self, data: SliceableBuffer) -> int: ...
    def toRaw(self) -> bytes: ...
    def __str__(self, indent: str = "") -> str: ...

class FixedFileInfo:
    sig: int
    strucVersion: int
    fileVersionMS: int
    fileVersionLS: int
    productVersionMS: int
    productVersionLS: int
    fileFlagsMask: int
    fileFlags: int
    fileOS: int
    fileType: int
    fileSubtype: int
    fileDateMS: int
    fileDateLS: int
    def __init__(
        self,
        filevers: _FourIntSequence = (0, 0, 0, 0),
        prodvers: _FourIntSequence = (0, 0, 0, 0),
        mask: int = 0x3F,
        flags: int = 0x0,
        OS: int = 0x40004,
        fileType: int = 0x1,
        subtype: int = 0x0,
        date: _TwoIntSequence = (0, 0),
    ) -> None: ...
    def fromRaw(self, data: SliceableBuffer, i: int) -> int: ...
    def toRaw(self) -> bytes: ...
    def __str__(self, indent: str = "") -> str: ...

class StringFileInfo:
    name: str
    kids: list[_Kid]
    def __init__(self, kids: list[_Kid] | None = None) -> None: ...
    def fromRaw(self, sublen: Unused, vallen: Unused, name: str, data: SliceableBuffer, i: int, limit: int) -> int: ...
    def toRaw(self) -> bytes: ...
    def __str__(self, indent: str = "") -> str: ...

class StringTable:
    name: str
    kids: list[_Kid]
    def __init__(self, name: str | None = None, kids: list[_Kid] | None = None) -> None: ...
    def fromRaw(self, data: SliceableBuffer, i: int, limit: int) -> int: ...
    def toRaw(self) -> bytes: ...
    def __str__(self, indent: str = "") -> str: ...

class StringStruct:
    name: str
    val: str
    def __init__(self, name: str | None = None, val: str | None = None) -> None: ...
    def fromRaw(self, data: SliceableBuffer, i: int, limit: int) -> int: ...
    def toRaw(self) -> bytes: ...
    def __str__(self, indent: Unused = "") -> str: ...

class VarFileInfo:
    kids: list[_Kid]
    def __init__(self, kids: list[_Kid] | None = None) -> None: ...
    sublen: int
    vallen: int
    name: str
    def fromRaw(self, sublen: int, vallen: int, name: str, data: SliceableBuffer, i: int, limit: int) -> int: ...
    wType: int
    def toRaw(self) -> bytes: ...
    def __str__(self, indent: str = "") -> str: ...

class VarStruct:
    name: str
    kids: list[Any]  # Whatever can be passed to struct.pack
    def __init__(self, name: str | None = None, kids: list[Any] | None = None) -> None: ...
    def fromRaw(self, data: SliceableBuffer, i: int, limit: Unused) -> int: ...
    wValueLength: int
    wType: int
    sublen: int
    def toRaw(self) -> bytes: ...
    def __str__(self, indent: Unused = "") -> str: ...
