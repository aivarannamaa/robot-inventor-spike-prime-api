"""
Module: '_api.button' on micropython-v1.14-893-lego learning system hub
"""
# MCU: {'machine': 'LEGO Technic Large Hub with STM32F413xx', 'sysname': 'LEGO Technic Large Hub', 'platform': 'LEGO Learning System Hub', 'nodename': 'LEGO Learning System Hub', 'ver': 'v1.14-893', 'release': '1.14.0', 'name': 'micropython', 'family': 'micropython', 'port': 'LEGO Learning System Hub', 'version': '1.14.0', 'mpy': 517, 'build': '893'}
# Stubber: 1.7.2
from typing import Any

from hub import _Button


class Button:
    """
    Instances of this class are available via PrimeHub / MSHub fields ``left_button`` or ``right_button``:

    ::

        from spike import PrimeHub
        // from mindstorms import MSHub

        hub = PrimeHub()
        // hub = MSHub()


        # Beep every time the Left Button is pressed

        while True:
            hub.left_button.wait_until_pressed()
            hub.speaker.start_beep()
            hub.left_button.wait_until_released()
            hub.speaker.stop()
    """

    def __init__(self, hub_button: _Button):
        """
        Constructor argument can be ``hub.button.left``, ``hub.button.right``, ``hub.button.center``, ``hub.button.connect``.
        """

    def is_pressed(self) -> bool:
        """"""

    def is_released(self) -> bool:
        """"""

    def wait_until_pressed(self) -> None:
        """"""

    def wait_until_released(self) -> None:
        """"""

    def was_pressed(self) -> bool:
        """
        Tests to see whether the button has been pressed since the last time this method called.
        Once this method returns "true," the button must be released and pressed again before it will return "true" again.
        """

