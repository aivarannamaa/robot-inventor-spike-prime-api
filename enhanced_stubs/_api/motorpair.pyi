"""
Module: '_api.motorpair' on micropython-v1.14-893-lego learning system hub
"""
# MCU: {'machine': 'LEGO Technic Large Hub with STM32F413xx', 'sysname': 'LEGO Technic Large Hub', 'platform': 'LEGO Learning System Hub', 'nodename': 'LEGO Learning System Hub', 'ver': 'v1.14-893', 'release': '1.14.0', 'name': 'micropython', 'family': 'micropython', 'port': 'LEGO Learning System Hub', 'version': '1.14.0', 'mpy': 517, 'build': '893'}
# Stubber: 1.7.2
from typing import Any, Optional, Dict

from hub import _Port

PORTS:Dict[str, _Port]

class MotorPair:
    BRAKE:str = "brake"
    COAST :str= "coast"
    HOLD :str= "hold"

    CM :str= "cm"
    IN :str= "in"
    DEGREES:str = "degrees"
    ROTATIONS:str = "rotations"
    SECONDS:str = "seconds"

    def __init__(self, port_1:str, port_2, str) -> None:
        """"""

    def move(self, amount:float, unit:str="cm", steering:int=0, speed:Optional[int]=None) -> None:
        """
        unit: one of "cm", "in", "rotations", "degrees", "seconds" (see constants in this class).
        steering: -100..100
        speed: -100..100 (None means default speed)
        """
    def start(self, steering:int=0, speed:Optional[int]=None) -> None:
        """"""
    def stop(self) -> None:
        """"""

    def move_tank(self, amount:float, unit:str="cm", left_speed:Optional[int]=None, right_speed:Optional[int]=None) -> None:
        """"""
    def start_tank(self,left_speed:int, right_speed:int) -> None:
        """"""
    def start_tank_at_power(self, left_power:int, right_power:int) -> None:
        """
        power: -100..100
        """

    def get_default_speed(self) -> int:
        """"""

    def set_motor_rotation(self, amount:float=17.6, unit:str="cm") -> None:
        """"""
    def set_default_speed(self, default_speed:int) -> None:
        """"""
    def set_stop_action(self, action:str="coast") -> None:
        """
        action: one of "coast", "brake", "hold"
        """

    def start_at_power(self, *args, **kwargs) -> Any:

        """"""
    def was_interrupted(self) -> bool:
        """"""

def clamp_power(*args, **kwargs) -> Any:
    """"""

def clamp_speed(*args, **kwargs) -> Any:
    """"""

def clamp_steering(*args, **kwargs) -> Any:
    """"""

def from_steering(*args, **kwargs) -> Any:
    """"""

