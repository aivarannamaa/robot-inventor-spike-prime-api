"""
Module: '_api.app' on micropython-v1.14-893-lego learning system hub
"""
# MCU: {'machine': 'LEGO Technic Large Hub with STM32F413xx', 'sysname': 'LEGO Technic Large Hub', 'platform': 'LEGO Learning System Hub', 'nodename': 'LEGO Learning System Hub', 'ver': 'v1.14-893', 'release': '1.14.0', 'name': 'micropython', 'family': 'micropython', 'port': 'LEGO Learning System Hub', 'version': '1.14.0', 'mpy': 517, 'build': '893'}
# Stubber: 1.7.2
from typing import Any

class App:
    """
    Instance of this class can be used for communicating with the official Mindstorms / Spike desktop app.
    Relevant only when the connection to the hub is made via the App.
    """

    def __init__(self) -> None:
        """"""
    def play_sound(self, name: str, volume: int = 100) -> None:
        """"""
    def start_sound(self, name: str, volume: int = 100) -> None:
        """"""
    def stop_sound(self, *args, **kwargs) -> Any:  # TODO:
        """"""
