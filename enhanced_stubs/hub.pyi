"""
Module: 'hub' on micropython-v1.14-893-lego learning system hub
"""
# MCU: {'machine': 'LEGO Technic Large Hub with STM32F413xx', 'sysname': 'LEGO Technic Large Hub', 'platform': 'LEGO Learning System Hub', 'nodename': 'LEGO Learning System Hub', 'ver': 'v1.14-893', 'release': '1.14.0', 'name': 'micropython', 'family': 'micropython', 'port': 'LEGO Learning System Hub', 'version': '1.14.0', 'mpy': 517, 'build': '893'}
# Stubber: 1.7.2
from typing import Any, Dict, overload, Tuple, Optional

__version__: str
config:Dict[str, Any] = {}

TOP:int = 0
FRONT:int = 1
RIGHT:int = 2
BOTTOM: int = 3
BACK: int = 4
LEFT = 5



class _Battery():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    BATTERY_BAD_BATTERY = -4 # type: int
    BATTERY_HUB_TEMPERATURE_CRITICAL_OUT_OF_RANGE = -2 # type: int
    BATTERY_MISSING = -6 # type: int
    BATTERY_NO_ERROR = 0 # type: int
    BATTERY_TEMPERATURE_OUT_OF_RANGE = -2 # type: int
    BATTERY_TEMPERATURE_SENSOR_FAIL = -3 # type: int
    BATTERY_VOLTAGE_TOO_LOW = -5 # type: int
    CHARGER_STATE_CHARGING_COMPLETED = 2 # type: int
    CHARGER_STATE_CHARGING_ONGOING = 1 # type: int
    CHARGER_STATE_DISCHARGING = 0 # type: int
    CHARGER_STATE_FAIL = -1 # type: int
    USB_CH_PORT_CDP = 2 # type: int
    USB_CH_PORT_DCP = 3 # type: int
    USB_CH_PORT_NONE = 0 # type: int
    USB_CH_PORT_SDP = 1 # type: int
    def capacity_left(self, *args, **kwargs) -> Any:
        """"""

    def charger_detect(self, *args, **kwargs) -> Any:
        """"""

    def current(self, *args, **kwargs) -> Any:
        """"""

    def info(self, *args, **kwargs) -> Any:
        """"""

    def temperature(self, *args, **kwargs) -> Any:
        """"""

    def voltage(self, *args, **kwargs) -> Any:
        """"""

class _Button():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def callback(self, *args, **kwargs) -> Any:
        """"""

    def is_pressed(self, *args, **kwargs) -> Any:
        """"""

    def on_change(self, *args, **kwargs) -> Any:
        """"""

    def presses(self, *args, **kwargs) -> Any:
        """"""

    def was_pressed(self, *args, **kwargs) -> Any:
        """"""


class _Bluetooth():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def discoverable(self, *args, **kwargs) -> Any:
        """"""

    def forget(self, *args, **kwargs) -> Any:
        """"""

    def info(self, *args, **kwargs) -> Any:
        """"""

    def lwp_advertise(self, *args, **kwargs) -> Any:
        """"""

    def lwp_bypass(self, *args, **kwargs) -> Any:
        """"""

    def lwp_monitor(self, *args, **kwargs) -> Any:
        """"""

    def rfcomm_connect(self, *args, **kwargs) -> Any:
        """"""

    def rfcomm_disconnect(self, *args, **kwargs) -> Any:
        """"""


class _Display():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def clear(self, *args, **kwargs) -> Any:
        """"""

    def align(self, *args, **kwargs) -> Any:
        """"""

    def callback(self, *args, **kwargs) -> Any:
        """"""

    def invert(self, *args, **kwargs) -> Any:
        """"""

    def pixel(self, *args, **kwargs) -> Any:
        """"""

    def rotation(self, *args, **kwargs) -> Any:
        """"""

    def show(self, *args, **kwargs) -> Any:
        """"""


class _Motion():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    DOUBLETAPPED = 1 # type: int
    FREEFALL = 3 # type: int
    SHAKE = 2 # type: int
    TAPPED = 0 # type: int
    def accelerometer(self, *args, **kwargs) -> Any:
        """"""

    def align_to_model(self, *args, **kwargs) -> Any:
        """"""

    def gesture(self, *args, **kwargs) -> Any:
        """"""

    def gyroscope(self, *args, **kwargs) -> Any:
        """"""

    def orientation(self, *args, **kwargs) -> Any:
        """"""

    def yaw_pitch_roll(self, *args, **kwargs) -> Any:
        """"""

class _Port():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def callback(self, *args, **kwargs) -> Any:
        """"""

    device : Any ## <class 'NoneType'> = None
    def info(self, *args, **kwargs) -> Any:
        """"""

    def mode(self, *args, **kwargs) -> Any:
        """"""

    motor : Any ## <class 'NoneType'> = None
    def pwm(self, *args, **kwargs) -> Any:
        """"""



class _Sound():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    SOUND_SAWTOOTH = 3 # type: int
    SOUND_SIN = 0 # type: int
    SOUND_SQUARE = 1 # type: int
    SOUND_TRIANGLE = 2 # type: int
    def beep(self, *args, **kwargs) -> Any:
        """"""

    def callback(self, *args, **kwargs) -> Any:
        """"""

    def play(self, *args, **kwargs) -> Any:
        """"""

    def volume(self, *args, **kwargs) -> Any:
        """"""


class _Supervision():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def callback(self, *args, **kwargs) -> Any:
        """"""

    def info(self, *args, **kwargs) -> Any:
        """"""

battery : Any ## <class 'Battery'> = Battery class
bluetooth : Any ## <class 'bluetooth'> = <bluetooth>
display : Any ## <class 'Display'> = <Display>
motion : Any ## <class 'Motion'> = Motion()


def info() -> Dict[str, Any]:
    """Returns information about the hub"""

def status() -> Dict[str, Any]:
    """Returns status of the components."""

@overload
def power_off(fast:bool=True, restart:bool=False) -> None:
    """
    Turns the hub off.

    Use fast=True for fast shut down, without the usual light animation and sound.
    Use restart=True to reboot after shutting down.
    """

@overload
def power_off(timeout:int=0) -> None:
    """Sets the inactivity timeout before the hub shuts down automatically."""

def repl_restart(restart: bool = True) -> None:
    """
    Resets the REPL and clears all variables if restart=True.

    Does nothing if restart=False.
    """

def temperature() -> float:
    """Returns hub's temperature in Celsius degrees."""


@overload
def led(color: int, /) -> None:
    """Sets the color of the LED in the center button of the hub.

    0 = off
    1 = pink
    2 = violet
    3 = blue
    4 = turquoise
    5 = light green
    6 = green
    7 = yellow
    8 = orange
    9 = red
    10 = white
    """

@overload
def led(red: int, green: int, blue: int, /) -> None:
    """Sets the color of the LED in the center button of the hub as RGB components (0-255)."""

@overload
def led(color:Tuple[int, int, int], /) -> None:
    """Sets the color of the LED in the center button of the hub as tuple of RGB components (0-255)."""


def file_transfer(filename: str, filesize: int, packetsize:int=1000, timeout:int=2000, mode:Optional[str]=None) -> None:
    """Prepares a file transfer to the hub."""

def reset() -> None:
    """Resets the hub."""




class Image():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    ALL_ARROWS: Tuple[Image, Image, Image, Image, Image, Image, Image, Image]
    ALL_CLOCKS: Tuple[Image, Image, Image, Image, Image, Image, Image, Image, Image, Image, Image, Image]
    ANGRY : Image ## <class 'Image'> = Image('90009:09090:00000:99999:90909:')
    ARROW_E : Image ## <class 'Image'> = Image('00900:00090:99999:00090:00900:')
    ARROW_N : Image ## <class 'Image'> = Image('00900:09990:90909:00900:00900:')
    ARROW_NE : Image ## <class 'Image'> = Image('00999:00099:00909:09000:90000:')
    ARROW_NW : Image ## <class 'Image'> = Image('99900:99000:90900:00090:00009:')
    ARROW_S : Image ## <class 'Image'> = Image('00900:00900:90909:09990:00900:')
    ARROW_SE : Image ## <class 'Image'> = Image('90000:09000:00909:00099:00999:')
    ARROW_SW : Image ## <class 'Image'> = Image('00009:00090:90900:99000:99900:')
    ARROW_W : Image ## <class 'Image'> = Image('00900:09000:99999:09000:00900:')
    ASLEEP : Image ## <class 'Image'> = Image('00000:99099:00000:09990:00000:')
    BUTTERFLY : Image ## <class 'Image'> = Image('99099:99999:00900:99999:99099:')
    CHESSBOARD : Image ## <class 'Image'> = Image('09090:90909:09090:90909:09090:')
    CLOCK1 : Image ## <class 'Image'> = Image('00090:00090:00900:00000:00000:')
    CLOCK10 : Image ## <class 'Image'> = Image('00000:99000:00900:00000:00000:')
    CLOCK11 : Image ## <class 'Image'> = Image('09000:09000:00900:00000:00000:')
    CLOCK12 : Image ## <class 'Image'> = Image('00900:00900:00900:00000:00000:')
    CLOCK2 : Image ## <class 'Image'> = Image('00000:00099:00900:00000:00000:')
    CLOCK3 : Image ## <class 'Image'> = Image('00000:00000:00999:00000:00000:')
    CLOCK4 : Image ## <class 'Image'> = Image('00000:00000:00900:00099:00000:')
    CLOCK5 : Image ## <class 'Image'> = Image('00000:00000:00900:00090:00090:')
    CLOCK6 : Image ## <class 'Image'> = Image('00000:00000:00900:00900:00900:')
    CLOCK7 : Image ## <class 'Image'> = Image('00000:00000:00900:09000:09000:')
    CLOCK8 : Image ## <class 'Image'> = Image('00000:00000:00900:99000:00000:')
    CLOCK9 : Image ## <class 'Image'> = Image('00000:00000:99900:00000:00000:')
    CONFUSED : Image ## <class 'Image'> = Image('00000:09090:00000:09090:90909:')
    COW : Image ## <class 'Image'> = Image('90009:90009:99999:09990:00900:')
    DIAMOND : Image ## <class 'Image'> = Image('00900:09090:90009:09090:00900:')
    DIAMOND_SMALL : Image ## <class 'Image'> = Image('00000:00900:09090:00900:00000:')
    DUCK : Image ## <class 'Image'> = Image('09900:99900:09999:09990:00000:')
    FABULOUS : Image ## <class 'Image'> = Image('99999:99099:00000:09090:09990:')
    GHOST : Image ## <class 'Image'> = Image('99999:90909:99999:99999:90909:')
    GIRAFFE : Image ## <class 'Image'> = Image('99000:09000:09000:09990:09090:')
    GO_DOWN : Image ## <class 'Image'> = Image('00000:99999:09990:00900:00000:')
    GO_LEFT : Image ## <class 'Image'> = Image('00090:00990:09990:00990:00090:')
    GO_RIGHT : Image ## <class 'Image'> = Image('09000:09900:09990:09900:09000:')
    GO_UP : Image ## <class 'Image'> = Image('00000:00900:09990:99999:00000:')
    HAPPY : Image ## <class 'Image'> = Image('00000:09090:00000:90009:09990:')
    HEART : Image ## <class 'Image'> = Image('09090:99999:99999:09990:00900:')
    HEART_SMALL : Image ## <class 'Image'> = Image('00000:09090:09990:00900:00000:')
    HOUSE : Image ## <class 'Image'> = Image('00900:09990:99999:09990:09090:')
    MEH : Image ## <class 'Image'> = Image('09090:00000:00090:00900:09000:')
    MUSIC_CROTCHET : Image ## <class 'Image'> = Image('00900:00900:00900:99900:99900:')
    MUSIC_QUAVER : Image ## <class 'Image'> = Image('00900:00990:00909:99900:99900:')
    MUSIC_QUAVERS : Image ## <class 'Image'> = Image('09999:09009:09009:99099:99099:')
    NO : Image ## <class 'Image'> = Image('90009:09090:00900:09090:90009:')
    PACMAN : Image ## <class 'Image'> = Image('09999:99090:99900:99990:09999:')
    PITCHFORK : Image ## <class 'Image'> = Image('90909:90909:99999:00900:00900:')
    RABBIT : Image ## <class 'Image'> = Image('90900:90900:99990:99090:99990:')
    ROLLERSKATE : Image ## <class 'Image'> = Image('00099:00099:99999:99999:09090:')
    SAD : Image ## <class 'Image'> = Image('00000:09090:00000:09990:90009:')
    SILLY : Image ## <class 'Image'> = Image('90009:00000:99999:00909:00999:')
    SKULL : Image ## <class 'Image'> = Image('09990:90909:99999:09990:09990:')
    SMILE : Image ## <class 'Image'> = Image('00000:00000:00000:90009:09990:')
    SNAKE : Image ## <class 'Image'> = Image('99000:99099:09090:09990:00000:')
    SQUARE : Image ## <class 'Image'> = Image('99999:90009:90009:90009:99999:')
    SQUARE_SMALL : Image ## <class 'Image'> = Image('00000:09990:09090:09990:00000:')
    STICKFIGURE : Image ## <class 'Image'> = Image('00900:99999:00900:09090:90009:')
    SURPRISED : Image ## <class 'Image'> = Image('09090:00000:00900:09090:00900:')
    SWORD : Image ## <class 'Image'> = Image('00900:00900:00900:09990:00900:')
    TARGET : Image ## <class 'Image'> = Image('00900:09990:99099:09990:00900:')
    TORTOISE : Image ## <class 'Image'> = Image('00000:09990:99999:09090:00000:')
    TRIANGLE : Image ## <class 'Image'> = Image('00000:00900:09090:99999:00000:')
    TRIANGLE_LEFT : Image ## <class 'Image'> = Image('90000:99000:90900:90090:99999:')
    TSHIRT : Image ## <class 'Image'> = Image('99099:99999:09990:09990:09990:')
    UMBRELLA : Image ## <class 'Image'> = Image('09990:99999:00900:90900:09900:')
    XMAS : Image ## <class 'Image'> = Image('00900:09990:00900:09990:99999:')
    YES : Image ## <class 'Image'> = Image('00000:00009:00090:90900:09000:')

    def get_pixel(self, *args, **kwargs) -> Any:
        """"""

    def height(self, *args, **kwargs) -> Any:
        """"""

    def set_pixel(self, *args, **kwargs) -> Any:
        """"""

    def shift_down(self, *args, **kwargs) -> Any:
        """"""

    def shift_left(self, *args, **kwargs) -> Any:
        """"""

    def shift_right(self, *args, **kwargs) -> Any:
        """"""

    def shift_up(self, *args, **kwargs) -> Any:
        """"""

    def width(self, *args, **kwargs) -> Any:
        """"""

class button():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    center : Any ## <class ''> = center
    connect : Any ## <class ''> = connect
    left : Any ## <class ''> = left
    right : Any ## <class ''> = right


class port():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    A : Any ## <class 'Port'> = Port(A)
    ATTACHED = 1 # type: int
    B : Any ## <class 'Port'> = Port(B)
    C : Any ## <class 'Port'> = Port(C)
    D : Any ## <class 'Port'> = Port(D)
    DETACHED = 0 # type: int
    E : Any ## <class 'Port'> = Port(E)
    F : Any ## <class 'Port'> = Port(F)
    MODE_DEFAULT = 0 # type: int
    MODE_FULL_DUPLEX = 1 # type: int
    MODE_GPIO = 3 # type: int
    MODE_HALF_DUPLEX = 2 # type: int

sound : Any ## <class 'Sound'> = Sound()

supervision : Any ## <class 'supervision'> = <supervision>


class BT_VCP():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def any(self, *args, **kwargs) -> Any:
        """"""

    def close(self, *args, **kwargs) -> Any:
        """"""

    def read(self, *args, **kwargs) -> Any:
        """"""

    def readinto(self, *args, **kwargs) -> Any:
        """"""

    def readline(self, *args, **kwargs) -> Any:
        """"""

    def send(self, *args, **kwargs) -> Any:
        """"""

    def write(self, *args, **kwargs) -> Any:
        """"""

    def callback(self, *args, **kwargs) -> Any:
        """"""

    def isconnected(self, *args, **kwargs) -> Any:
        """"""

    def readlines(self, *args, **kwargs) -> Any:
        """"""

    def recv(self, *args, **kwargs) -> Any:
        """"""

    def setinterrupt(self, *args, **kwargs) -> Any:
        """"""

class USB_VCP():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def any(self, *args, **kwargs) -> Any:
        """"""

    def close(self, *args, **kwargs) -> Any:
        """"""

    def read(self, *args, **kwargs) -> Any:
        """"""

    def readinto(self, *args, **kwargs) -> Any:
        """"""

    def readline(self, *args, **kwargs) -> Any:
        """"""

    def send(self, *args, **kwargs) -> Any:
        """"""

    def write(self, *args, **kwargs) -> Any:
        """"""

    CTS = 2 # type: int
    RTS = 1 # type: int
    def callback(self, *args, **kwargs) -> Any:
        """"""

    def init(self, *args, **kwargs) -> Any:
        """"""

    def isconnected(self, *args, **kwargs) -> Any:
        """"""

    def readlines(self, *args, **kwargs) -> Any:
        """"""

    def recv(self, *args, **kwargs) -> Any:
        """"""

    def setinterrupt(self, *args, **kwargs) -> Any:
        """"""

