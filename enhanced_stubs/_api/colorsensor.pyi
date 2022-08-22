"""
Module: '_api.colorsensor' on micropython-v1.14-893-lego learning system hub
"""
# MCU: {'machine': 'LEGO Technic Large Hub with STM32F413xx', 'sysname': 'LEGO Technic Large Hub', 'platform': 'LEGO Learning System Hub', 'nodename': 'LEGO Learning System Hub', 'ver': 'v1.14-893', 'release': '1.14.0', 'name': 'micropython', 'family': 'micropython', 'port': 'LEGO Learning System Hub', 'version': '1.14.0', 'mpy': 517, 'build': '893'}
# Stubber: 1.7.2
from typing import Any, Optional, Tuple

class ColorSensor:
    def __init__(self, port: str) -> None:
        """"""
    def get_color(self) -> Optional[str]:
        """
        Retrieves the detected color of a surface.

        Returns one of 'black','violet','blue','cyan','green','yellow','red','white',None
        """
    def get_ambient_light(self) -> int:
        """
        Retrieves the intensity of the ambient light.

        This causes the Color Sensor to change modes, which can affect your program in unexpected ways.
        For example, the Color Sensor can't read colors when it's in ambient light mode.

        Returns min 0, max 100
        """
    def get_reflected_light(self) -> int:
        """
        Retrieves the intensity of the reflected light.

        Returns 0..100
        """
    def get_rgb_intensity(self) -> Tuple[int, int, int, int]:
        """
        Retrieves the overall color intensity, and intensity of red, green, and blue.

        Returns Red, green, blue, and overall intensity (0-1024)
        """
    def get_red(self) -> int:
        """
        Retrieves the color intensity of red.

        Returns 0..1024.
        """
    def get_green(self) -> int:
        """
        Retrieves the color intensity of green.

        Returns 0..1024.
        """
    def get_blue(self) -> int:
        """
        Retrieves the color intensity of blue.

        Returns 0..1024.
        """
    def wait_until_color(self, color: Optional[str]) -> None:
        """
        Waits until the Color Sensor detects the specified color.

        Accepted values: "black","violet","blue","cyan","green","yellow","red","white",None
        """
    def light_up(self, *args, **kwargs) -> Any:
        """"""
    def light_up_all(self, *args, **kwargs) -> Any:
        """"""
    def wait_for_new_color(self, *args, **kwargs) -> Any:
        """"""

LPF2_FLIPPER_COLOR = 61  # type: int
PORTS = {}  # type: dict

def clamp(*args, **kwargs) -> Any:
    """"""

def get_sensor_value(*args, **kwargs) -> Any:
    """"""

def is_type(*args, **kwargs) -> Any:
    """"""

def newSensorDisconnectedError(*args, **kwargs) -> Any:
    """"""

def sleep_ms(*args, **kwargs) -> Any:
    """"""
