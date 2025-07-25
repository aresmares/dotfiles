from collections.abc import Iterable, Iterator, Mapping
from typing import Any, ClassVar
from typing_extensions import Self

from numpy import ndarray
from scipy.sparse import spmatrix

from .._typing import ArrayLike, MatrixLike
from ..base import BaseEstimator, TransformerMixin

# Authors: Lars Buitinck
#          Dan Blanchard <dblanchard@ets.org>
# License: BSD 3 clause

class DictVectorizer(TransformerMixin, BaseEstimator):
    feature_names_: list = ...
    vocabulary_: dict = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, *, dtype=..., separator: str = "=", sparse: bool = True, sort: bool = True) -> None: ...
    def fit(self, X: Mapping | Iterable[Mapping], y: Any = None) -> Self: ...
    def fit_transform(
        self,
        X: Iterator[Any] | Mapping | Iterable[Mapping] | list[dict[str, int]],
        y: Any = None,
    ) -> ndarray | spmatrix: ...
    def inverse_transform(self, X: MatrixLike | ArrayLike, dict_type=...) -> list[Mapping]: ...
    def transform(self, X: ArrayLike | Mapping[str, ArrayLike] | Iterator[Mapping[str, ArrayLike]]) -> ndarray | spmatrix: ...
    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray: ...
    def restrict(self, support: ArrayLike, indices: bool = False) -> Self: ...
