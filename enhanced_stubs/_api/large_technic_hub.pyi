"""
Module: '_api.large_technic_hub' on micropython-v1.14-893-lego learning system hub
"""
# MCU: {'machine': 'LEGO Technic Large Hub with STM32F413xx', 'sysname': 'LEGO Technic Large Hub', 'platform': 'LEGO Learning System Hub', 'nodename': 'LEGO Learning System Hub', 'ver': 'v1.14-893', 'release': '1.14.0', 'name': 'micropython', 'family': 'micropython', 'port': 'LEGO Learning System Hub', 'version': '1.14.0', 'mpy': 517, 'build': '893'}
# Stubber: 1.7.2

from .button import Button
from .lightmatrix import LightMatrix
from .motionsensor import MotionSensor
from .speaker import Speaker
from .statuslight import StatusLight


class LargeTechnicHub():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    PORT_A:str = 'A'
    PORT_B:str = 'B'
    PORT_C:str = 'C'
    PORT_D:str = 'D'
    PORT_E:str = 'E'
    PORT_F:str = 'F'

    left_button : Button
    light_matrix : LightMatrix
    motion_sensor : MotionSensor
    right_button : Button
    speaker : Speaker
    status_light : StatusLight

