import ast
from argparse import Namespace
from collections.abc import Iterator
from typing import ClassVar
from typing_extensions import TypeAlias

from flake8.options.manager import OptionManager

_Error: TypeAlias = tuple[int, int, str, type[BuiltinsChecker]]

class BuiltinsChecker:
    name: ClassVar[str]
    version: ClassVar[str]
    assign_msg: ClassVar[str]
    argument_msg: ClassVar[str]
    class_attribute_msg: ClassVar[str]
    import_msg: ClassVar[str]
    module_name_msg: ClassVar[str]
    lambda_argument_msg: ClassVar[str]

    names: ClassVar[list[str]]
    ignore_list: ClassVar[set[str]]
    ignored_module_names: ClassVar[set[str]]

    def __init__(self, tree: ast.AST, filename: str) -> None: ...
    @classmethod
    def add_options(cls, option_manager: OptionManager) -> None: ...
    @classmethod
    def parse_options(cls, options: Namespace) -> None: ...
    def run(self) -> Iterator[_Error]: ...
    def check_assignment(self, statement: ast.Assign | ast.AnnAssign | ast.NamedExpr) -> Iterator[_Error]: ...
    def check_function_definition(self, statement: ast.FunctionDef | ast.AsyncFunctionDef) -> Iterator[_Error]: ...
    def check_lambda_definition(self, statement: ast.Lambda) -> Iterator[_Error]: ...
    def check_for_loop(self, statement: ast.For | ast.AsyncFor) -> Iterator[_Error]: ...
    def check_with(self, statement: ast.With | ast.AsyncWith) -> Iterator[_Error]: ...
    def check_exception(self, statement: ast.excepthandler) -> Iterator[_Error]: ...
    def check_comprehension(
        self, statement: ast.ListComp | ast.SetComp | ast.DictComp | ast.GeneratorExp
    ) -> Iterator[_Error]: ...
    def check_import(self, statement: ast.Import | ast.ImportFrom) -> Iterator[_Error]: ...
    def check_class(self, statement: ast.ClassDef) -> Iterator[_Error]: ...
    def error(self, statement: ast.AST | None = None, variable: str | None = None, message: str | None = None) -> _Error: ...
    def check_module_name(self, filename: str) -> Iterator[_Error]: ...
