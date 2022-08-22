from typing import Any, Callable


class Timer:
    def __init__(self) -> None:
        """"""

    def now(self) -> int:
        """"""
    def reset(self) -> None:
        """"""

def wait_for_seconds(seconds: float) -> None:
    """"""

def wait_until(get_value_function: Callable[[], Any],
               operator_function: Callable[[Any, Any], bool],
               target_value: Any) -> None:
    """"""
