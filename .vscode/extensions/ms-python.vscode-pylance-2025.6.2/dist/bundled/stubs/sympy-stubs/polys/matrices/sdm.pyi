import sys
from typing import Any
from typing_extensions import Self, TypeAlias

from sympy.polys.matrices.ddm import DDM

if sys.version_info >= (3, 10):
    from types import NotImplementedType
else:
    NotImplementedType: TypeAlias = Any

class SDM(dict):
    fmt = ...
    def __init__(self, elemsdict, shape, domain) -> None: ...
    def getitem(self, i, j): ...
    def setitem(self, i, j, value) -> None: ...
    def extract_slice(self, slice1, slice2) -> Self: ...
    def extract(self, rows, cols) -> Self: ...
    @classmethod
    def new(cls, sdm, shape, domain) -> Self: ...
    def copy(A) -> Self: ...
    @classmethod
    def from_list(cls, ddm, shape, domain) -> Self: ...
    @classmethod
    def from_ddm(cls, ddm) -> Self: ...
    def to_list(M) -> list[Any]: ...
    def to_list_flat(M): ...
    def to_dok(M) -> dict[tuple[Any, Any], Any]: ...
    def to_ddm(M) -> DDM: ...
    def to_sdm(M) -> Self: ...
    @classmethod
    def zeros(cls, shape, domain) -> Self: ...
    @classmethod
    def ones(cls, shape, domain) -> Self: ...
    @classmethod
    def eye(cls, shape, domain) -> Self: ...
    @classmethod
    def diag(cls, diagonal, domain, shape) -> Self: ...
    def transpose(M) -> Self: ...
    def __add__(A, B) -> NotImplementedType | Self: ...
    def __sub__(A, B) -> NotImplementedType | Self: ...
    def __neg__(A) -> Self: ...
    def __mul__(A, B) -> Self | NotImplementedType: ...
    def __rmul__(a, b) -> Self | NotImplementedType: ...
    def matmul(A, B) -> Self: ...
    def mul(A, b) -> Self: ...
    def rmul(A, b) -> Self: ...
    def mul_elementwise(A, B) -> Self: ...
    def add(A, B) -> Self: ...
    def sub(A, B) -> Self: ...
    def neg(A) -> Self: ...
    def convert_to(A, K) -> Self: ...
    def scc(A) -> list[Any]: ...
    def rref(A) -> tuple[Self, list[Any]]: ...
    def inv(A) -> Self: ...
    def det(A): ...
    def lu(A) -> tuple[Self, Self, list[Any]]: ...
    def lu_solve(A, b) -> Self: ...
    def nullspace(A) -> tuple[Self, list[int]]: ...
    def particular(A) -> Self: ...
    def hstack(A, *B) -> Self: ...
    def vstack(A, *B) -> Self: ...
    def applyfunc(self, func, domain) -> Self: ...
    def charpoly(A) -> list[Any]: ...
    def is_zero_matrix(self) -> bool: ...
    def is_upper(self) -> bool: ...
    def is_lower(self) -> bool: ...
    def lll(A, delta=...) -> Self: ...
    def lll_transform(A, delta=...) -> tuple[Self, Self]: ...

def binop_dict(A, B, fab, fa, fb) -> dict[Any, Any]: ...
def unop_dict(A, f) -> dict[Any, Any]: ...
def sdm_transpose(M) -> dict[Any, Any]: ...
def sdm_matmul(A, B, K, m, o) -> dict[Any, Any]: ...
def sdm_matmul_exraw(A, B, K, m, o) -> dict[Any, Any]: ...
def sdm_irref(A) -> tuple[dict[int, Any], list[Any], dict[Any, set[int]]]: ...
def sdm_nullspace_from_rref(A, one, ncols, pivots, nonzero_cols) -> tuple[list[Any], list[int]]: ...
def sdm_particular_from_rref(A, ncols, pivots) -> dict[Any, Any]: ...
