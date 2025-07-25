from typing import ClassVar

from numpy import ndarray

from ..._typing import ArrayLike, Float, Int, MatrixLike
from .histogram import HistogramBuilder
from .predictor import TreePredictor
from .splitting import SplitInfo, Splitter

EPS = ...  # to avoid zero division errors

class TreeNode:
    children_upper_bound: float = ...
    children_lower_bound: float = ...
    interaction_cst_indices: None | list[int] = ...
    allowed_features: None | ndarray = ...
    value: float | None = ...
    is_leaf: bool = ...
    sum_hessians: float = ...
    sum_gradients: float = ...
    sample_indices: ndarray = ...
    depth: int = ...

    split_info: ClassVar[None | SplitInfo] = ...
    left_child: ClassVar[TreeNode | None] = ...
    right_child: ClassVar[TreeNode | None] = ...
    histograms = ...

    # start and stop indices of the node in the splitter.partition
    # array. Concretely,
    # self.sample_indices = view(self.splitter.partition[start:stop])
    # Please see the comments about splitter.partition and
    # splitter.split_indices for more info about this design.
    # These 2 attributes are only used in _update_raw_prediction, because we
    # need to iterate over the leaves and I don't know how to efficiently
    # store the sample_indices views because they're all of different sizes.
    partition_start: ClassVar[int] = ...
    partition_stop: ClassVar[int] = ...

    def __init__(
        self,
        depth: Int,
        sample_indices: ArrayLike,
        sum_gradients: Float,
        sum_hessians: Float,
        value=None,
    ) -> None: ...
    def set_children_bounds(self, lower: float, upper: float) -> None: ...
    def __lt__(self, other_node: TreeNode) -> bool: ...

class TreeGrower:
    with_monotonic_cst: bool = ...
    total_apply_split_time: float = ...
    total_compute_hist_time: float = ...
    total_find_split_time: float = ...
    n_nodes: int = ...
    n_features: int = ...
    n_categorical_splits: int = ...
    missing_values_bin_idx: int = ...
    splittable_nodes: list[TreeNode] = ...
    finalized_leaves: list[TreeNode] = ...
    root: TreeNode = ...
    splitter: Splitter = ...
    histogram_builder: HistogramBuilder = ...

    def __init__(
        self,
        X_binned: MatrixLike,
        gradients: ArrayLike,
        hessians: ArrayLike,
        max_leaf_nodes: None | Int = None,
        max_depth: None | Int = None,
        min_samples_leaf: Int = 20,
        min_gain_to_split: Float = 0.0,
        n_bins: Int = 256,
        n_bins_non_missing: None | ArrayLike = None,
        has_missing_values: ndarray | ArrayLike | bool = False,
        is_categorical: None | ArrayLike = None,
        monotonic_cst: None | ArrayLike = None,
        interaction_cst: list[set[int]] | None = None,
        l2_regularization: Float = 0.0,
        min_hessian_to_split: Float = 1e-3,
        shrinkage: Float = 1.0,
        n_threads: None | Int = None,
    ) -> None: ...
    def grow(self) -> None: ...
    def split_next(self) -> tuple[TreeNode, TreeNode]: ...
    def make_predictor(self, binning_thresholds: ArrayLike) -> TreePredictor: ...
