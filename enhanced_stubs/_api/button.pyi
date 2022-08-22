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
