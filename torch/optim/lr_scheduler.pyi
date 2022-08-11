from typing import Iterable, Any, Optional, Callable, Union, List
from .optimizer import Optimizer

class _LRScheduler:
    optimizer: Optimizer = ...
    base_lrs: List[float] = ...
    last_epoch: int = ...
    verbose: bool = ...
    def __init__(self, optimizer: Optimizer, last_epoch: int = ..., verbose: bool = ...) -> None: ...
    def state_dict(self) -> dict: ...
    def load_state_dict(self, state_dict: dict) -> None: ...
    def get_last_lr(self) -> List[float]: ...
    def get_lr(self) -> float: ...
    def step(self, epoch: Optional[int] = ...) -> None: ...
    def print_lr(self, is_verbose: bool, group: dict, lr: float, epoch: Optional[int] = ...) -> None: ...

class LambdaLR(_LRScheduler):
    lr_lambdas: List[Callable[[int], float]] = ...
    def __init__(self, optimizer: Optimizer, lr_lambda: Union[Callable[[int], float], List[Callable[[int], float]]], last_epoch: int = ..., verbose: bool = ...) -> None: ...

class MultiplicativeLR(_LRScheduler):
    lr_lambdas: List[Callable[[int], float]] = ...
    def __init__(self, optimizer: Optimizer, lr_lambda: Union[Callable[[int], float], List[Callable[[int], float]]], last_epoch: int = ..., verbose: bool = ...) -> None: ...

class StepLR(_LRScheduler):
    step_size: int = ...
    gamma: float = ...
    def __init__(self, optimizer: Optimizer, step_size: int, gamma: float = ..., last_epoch: int = ..., verbose: bool = ...) -> None: ...

class MultiStepLR(_LRScheduler):
    milestones: Iterable[int] = ...
    gamma: float = ...
    def __init__(self, optimizer: Optimizer, milestones: Iterable[int], gamma: float = ..., last_epoch: int = ..., verbose: bool = ...) -> None: ...

class ConstantLR(_LRScheduler):
    factor: float = ...
    total_iters: int = ...
    def __init__(self, optimizer: Optimizer, factor: float=..., total_iters: int=..., last_epoch: int=..., verbose: bool = ...) -> None: ...

class LinearLR(_LRScheduler):
    start_factor: float = ...
    end_factor: float = ...
    total_iters: int = ...
    def __init__(self, optimizer: Optimizer, start_factor: float=..., end_factor: float= ..., total_iters: int= ..., last_epoch: int= ..., verbose: bool = ...) -> None: ...

class ExponentialLR(_LRScheduler):
    gamma: float = ...
    def __init__(self, optimizer: Optimizer, gamma: float, last_epoch: int = ..., verbose: bool = ...) -> None: ...

class ChainedScheduler(_LRScheduler):
    def __init__(self, schedulers: List[_LRScheduler]) -> None: ...

class SequentialLR(_LRScheduler):
    def __init__(self, optimizer: Optimizer, schedulers: List[_LRScheduler], milestones: List[int], last_epoch: int=..., verbose: bool=...) -> None: ...

class CosineAnnealingLR(_LRScheduler):
    T_max: int = ...
    eta_min: float = ...
    def __init__(self, optimizer: Optimizer, T_max: int, eta_min: float = ..., last_epoch: int = ..., verbose: bool = ...) -> None: ...

class ReduceLROnPlateau:
    factor: float = ...
    optimizer: Optimizer = ...
    min_lrs: List[float] = ...
    patience: int = ...
    verbose: bool = ...
    cooldown: int = ...
    cooldown_counter: int = ...
    mode: str = ...
    threshold: float = ...
    threshold_mode: str = ...
    best: Optional[float] = ...
    num_bad_epochs: Optional[int] = ...
    mode_worse: Optional[float] = ...
    eps: float = ...
    last_epoch: int = ...
    def __init__(self, optimizer: Optimizer, mode: str = ..., factor: float = ..., patience: int = ..., threshold: float = ..., threshold_mode: str = ..., cooldown: int = ..., min_lr: Union[List[float], float] = ..., eps: float = ..., verbose: bool = ...) -> None: ...
    def step(self, metrics: Any, epoch: Optional[int] = ...) -> None: ...
    @property
    def in_cooldown(self) -> bool: ...
    def is_better(self, a: Any, best: Any) -> bool: ...
    def state_dict(self) -> dict: ...
    def load_state_dict(self, state_dict: dict) -> None: ...

class CyclicLR(_LRScheduler):
    max_lrs: List[float] = ...
    total_size: float = ...
    step_ratio: float = ...
    mode: str = ...
    gamma: float = ...
    scale_fn: Any = ...
    scale_mode: str = ...
    cycle_momentum: bool = ...
    base_momentums: List[float] = ...
    max_momentums: List[float] = ...
    def __init__(self, optimizer: Optimizer, base_lr: Union[float, List[float]], max_lr: Union[float, List[float]], step_size_up: int = ..., step_size_down: Optional[int] = ..., mode: str = ..., gamma: float = ..., scale_fn: Optional[Callable[[float], float]] = ..., scale_mode: str = ..., cycle_momentum: bool = ..., base_momentum: float = ..., max_momentum: float = ..., last_epoch: int = ..., verbose: bool = ...) -> None: ...

class CosineAnnealingWarmRestarts(_LRScheduler):
    T_0: int = ...
    T_i: int = ...
    T_mult: Optional[int] = ...
    eta_min: Optional[float] = ...
    T_cur: Any = ...
    def __init__(self, optimizer: Optimizer, T_0: int, T_mult: int = ..., eta_min: float = ..., last_epoch: int = ..., verbose: bool = ...) -> None: ...
    def step(self, epoch: Optional[Any] = ...): ...

class OneCycleLR(_LRScheduler):
    total_steps: int = ...
    anneal_func: Callable[[float, float, float], float] = ...
    cycle_momentum: bool = ...
    use_beta1: bool = ...
    def __init__(self, optimizer: Optimizer, max_lr: Union[float, List[float]], total_steps: int = ..., epochs: int = ..., steps_per_epoch: int = ..., pct_start: float = ..., anneal_strategy: str = ..., cycle_momentum: bool = ..., base_momentum: Union[float, List[float]] = ..., max_momentum: Union[float, List[float]] = ..., div_factor: float = ..., final_div_factor: float = ..., three_phase: bool = ..., last_epoch: int = ..., verbose: bool = ...) -> None: ...

class PolynomialLR(_LRScheduler):
    total_iters: int = ...
    power: float = ...
    def __init__(self, optimizer: Optimizer, total_iters: int = ..., power: float = ..., last_epoch: int = ..., verbose: bool = ...) -> None: ...
