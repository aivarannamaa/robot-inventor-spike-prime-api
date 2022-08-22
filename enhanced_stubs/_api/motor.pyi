from typing import Any, Tuple, Dict, Optional

from hub import _Port

MOTOR_TYPES:Tuple
PORTS:Dict[str, _Port]


class Motor:
    BRAKE:str = "brake"
    COAST:str = "coast"
    HOLD:str = "hold"

    def __init__(self, port:str) -> None:
        """"""
    def run_to_position(self, degrees:int, direction:str="shortest_path", speed:Optional[int]=None) -> None:
        """
        direction: one of "shortest path", "clockwise", "counterclockwise"
        degrees: 0-359
        speed: 1-100 (None means default speed)
        """
    def run_to_degrees_counted(self, degrees:int, speed:Optional[int]=None) -> None:
        """"""
    def run_for_degrees(self, degrees:int, speed:Optional[int]=None) -> None:
        """
        speed: -100..100
        """
    def run_for_rotations(self, rotations:float, speed:Optional[int]=None) -> None:
        """
        speed: -100..100
        """
    def run_for_seconds(self, seconds:float, speed:Optional[int]=None) -> None:
        """"""
    def start(self, speed:Optional[int]=None) -> None:
        """"""
    def start_at_power(self, power:int) -> None:
        """
        power: -100..100
        """
    def stop(self) -> None:
        """"""

    def get_speed(self) -> int:
        """"""
    def get_position(self) -> int:
        """"""
    def get_degrees_counted(self) -> int:
        """"""
    def get_default_speed(self) -> int:
        """"""

    def was_interrupted(self) -> bool:
        """"""
    def was_stalled(self) -> bool:
        """"""

    def set_degrees_counted(self, degrees_counted:int) -> None:
        """"""
    def set_default_speed(self, default_speed:int) -> None:
        """
        default_speed: -100..100
        """
    def set_stop_action(self, action:str) -> None:
        """
        action: one of "coast", "brake", "hold" (can be specified as string literals or via constants
        in this class)
        """
    def set_stall_detection(self, stop_when_stalled:bool=True) -> None:
        """"""

def clamp_power(*args, **kwargs) -> Any:
    """"""

def clamp_speed(*args, **kwargs) -> Any:
    """"""
