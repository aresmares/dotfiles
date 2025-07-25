from _typeshed import Unused

class DescriptorPool:
    def __new__(cls, descriptor_db=None): ...
    def __init__(  # pyright: ignore[reportInconsistentConstructor]
        self, descriptor_db=None, use_deprecated_legacy_json_field_conflicts: Unused = False
    ) -> None: ...
    def Add(self, file_desc_proto): ...
    def AddSerializedFile(self, serialized_file_desc_proto): ...
    def FindFileByName(self, file_name): ...
    def FindFileContainingSymbol(self, symbol): ...
    def FindMessageTypeByName(self, full_name): ...
    def FindEnumTypeByName(self, full_name): ...
    def FindFieldByName(self, full_name): ...
    def FindOneofByName(self, full_name): ...
    def FindExtensionByName(self, full_name): ...
    def FindExtensionByNumber(self, message_descriptor, number): ...
    def FindAllExtensions(self, message_descriptor): ...
    def FindServiceByName(self, full_name): ...
    def FindMethodByName(self, full_name): ...

def Default(): ...
