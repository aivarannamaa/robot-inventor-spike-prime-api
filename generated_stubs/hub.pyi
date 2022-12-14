"""
Module: 'hub' on micropython-v1.14-893-lego learning system hub
"""
# MCU: {'machine': 'LEGO Technic Large Hub with STM32F413xx', 'sysname': 'LEGO Technic Large Hub', 'platform': 'LEGO Learning System Hub', 'nodename': 'LEGO Learning System Hub', 'ver': 'v1.14-893', 'release': '1.14.0', 'name': 'micropython', 'family': 'micropython', 'port': 'LEGO Learning System Hub', 'version': '1.14.0', 'mpy': 517, 'build': '893'}
# Stubber: 1.7.2
from typing import Any

BACK = 4 # type: int
BOTTOM = 3 # type: int

class BT_VCP():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def any(self, *args, **kwargs) -> Any:
        """"""

    def callback(self, *args, **kwargs) -> Any:
        """"""

    def close(self, *args, **kwargs) -> Any:
        """"""

    def isconnected(self, *args, **kwargs) -> Any:
        """"""

    def read(self, *args, **kwargs) -> Any:
        """"""

    def readinto(self, *args, **kwargs) -> Any:
        """"""

    def readline(self, *args, **kwargs) -> Any:
        """"""

    def readlines(self, *args, **kwargs) -> Any:
        """"""

    def recv(self, *args, **kwargs) -> Any:
        """"""

    def send(self, *args, **kwargs) -> Any:
        """"""

    def setinterrupt(self, *args, **kwargs) -> Any:
        """"""

    def write(self, *args, **kwargs) -> Any:
        """"""

FRONT = 1 # type: int

class Image():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    ALL_ARROWS = () # type: tuple
    ALL_CLOCKS = () # type: tuple
    ANGRY : Any ## <class 'Image'> = Image('90009:09090:00000:99999:90909:')
    ARROW_E : Any ## <class 'Image'> = Image('00900:00090:99999:00090:00900:')
    ARROW_N : Any ## <class 'Image'> = Image('00900:09990:90909:00900:00900:')
    ARROW_NE : Any ## <class 'Image'> = Image('00999:00099:00909:09000:90000:')
    ARROW_NW : Any ## <class 'Image'> = Image('99900:99000:90900:00090:00009:')
    ARROW_S : Any ## <class 'Image'> = Image('00900:00900:90909:09990:00900:')
    ARROW_SE : Any ## <class 'Image'> = Image('90000:09000:00909:00099:00999:')
    ARROW_SW : Any ## <class 'Image'> = Image('00009:00090:90900:99000:99900:')
    ARROW_W : Any ## <class 'Image'> = Image('00900:09000:99999:09000:00900:')
    ASLEEP : Any ## <class 'Image'> = Image('00000:99099:00000:09990:00000:')
    BUTTERFLY : Any ## <class 'Image'> = Image('99099:99999:00900:99999:99099:')
    CHESSBOARD : Any ## <class 'Image'> = Image('09090:90909:09090:90909:09090:')
    CLOCK1 : Any ## <class 'Image'> = Image('00090:00090:00900:00000:00000:')
    CLOCK10 : Any ## <class 'Image'> = Image('00000:99000:00900:00000:00000:')
    CLOCK11 : Any ## <class 'Image'> = Image('09000:09000:00900:00000:00000:')
    CLOCK12 : Any ## <class 'Image'> = Image('00900:00900:00900:00000:00000:')
    CLOCK2 : Any ## <class 'Image'> = Image('00000:00099:00900:00000:00000:')
    CLOCK3 : Any ## <class 'Image'> = Image('00000:00000:00999:00000:00000:')
    CLOCK4 : Any ## <class 'Image'> = Image('00000:00000:00900:00099:00000:')
    CLOCK5 : Any ## <class 'Image'> = Image('00000:00000:00900:00090:00090:')
    CLOCK6 : Any ## <class 'Image'> = Image('00000:00000:00900:00900:00900:')
    CLOCK7 : Any ## <class 'Image'> = Image('00000:00000:00900:09000:09000:')
    CLOCK8 : Any ## <class 'Image'> = Image('00000:00000:00900:99000:00000:')
    CLOCK9 : Any ## <class 'Image'> = Image('00000:00000:99900:00000:00000:')
    CONFUSED : Any ## <class 'Image'> = Image('00000:09090:00000:09090:90909:')
    COW : Any ## <class 'Image'> = Image('90009:90009:99999:09990:00900:')
    DIAMOND : Any ## <class 'Image'> = Image('00900:09090:90009:09090:00900:')
    DIAMOND_SMALL : Any ## <class 'Image'> = Image('00000:00900:09090:00900:00000:')
    DUCK : Any ## <class 'Image'> = Image('09900:99900:09999:09990:00000:')
    FABULOUS : Any ## <class 'Image'> = Image('99999:99099:00000:09090:09990:')
    GHOST : Any ## <class 'Image'> = Image('99999:90909:99999:99999:90909:')
    GIRAFFE : Any ## <class 'Image'> = Image('99000:09000:09000:09990:09090:')
    GO_DOWN : Any ## <class 'Image'> = Image('00000:99999:09990:00900:00000:')
    GO_LEFT : Any ## <class 'Image'> = Image('00090:00990:09990:00990:00090:')
    GO_RIGHT : Any ## <class 'Image'> = Image('09000:09900:09990:09900:09000:')
    GO_UP : Any ## <class 'Image'> = Image('00000:00900:09990:99999:00000:')
    HAPPY : Any ## <class 'Image'> = Image('00000:09090:00000:90009:09990:')
    HEART : Any ## <class 'Image'> = Image('09090:99999:99999:09990:00900:')
    HEART_SMALL : Any ## <class 'Image'> = Image('00000:09090:09990:00900:00000:')
    HOUSE : Any ## <class 'Image'> = Image('00900:09990:99999:09990:09090:')
    MEH : Any ## <class 'Image'> = Image('09090:00000:00090:00900:09000:')
    MUSIC_CROTCHET : Any ## <class 'Image'> = Image('00900:00900:00900:99900:99900:')
    MUSIC_QUAVER : Any ## <class 'Image'> = Image('00900:00990:00909:99900:99900:')
    MUSIC_QUAVERS : Any ## <class 'Image'> = Image('09999:09009:09009:99099:99099:')
    NO : Any ## <class 'Image'> = Image('90009:09090:00900:09090:90009:')
    PACMAN : Any ## <class 'Image'> = Image('09999:99090:99900:99990:09999:')
    PITCHFORK : Any ## <class 'Image'> = Image('90909:90909:99999:00900:00900:')
    RABBIT : Any ## <class 'Image'> = Image('90900:90900:99990:99090:99990:')
    ROLLERSKATE : Any ## <class 'Image'> = Image('00099:00099:99999:99999:09090:')
    SAD : Any ## <class 'Image'> = Image('00000:09090:00000:09990:90009:')
    SILLY : Any ## <class 'Image'> = Image('90009:00000:99999:00909:00999:')
    SKULL : Any ## <class 'Image'> = Image('09990:90909:99999:09990:09990:')
    SMILE : Any ## <class 'Image'> = Image('00000:00000:00000:90009:09990:')
    SNAKE : Any ## <class 'Image'> = Image('99000:99099:09090:09990:00000:')
    SQUARE : Any ## <class 'Image'> = Image('99999:90009:90009:90009:99999:')
    SQUARE_SMALL : Any ## <class 'Image'> = Image('00000:09990:09090:09990:00000:')
    STICKFIGURE : Any ## <class 'Image'> = Image('00900:99999:00900:09090:90009:')
    SURPRISED : Any ## <class 'Image'> = Image('09090:00000:00900:09090:00900:')
    SWORD : Any ## <class 'Image'> = Image('00900:00900:00900:09990:00900:')
    TARGET : Any ## <class 'Image'> = Image('00900:09990:99099:09990:00900:')
    TORTOISE : Any ## <class 'Image'> = Image('00000:09990:99999:09090:00000:')
    TRIANGLE : Any ## <class 'Image'> = Image('00000:00900:09090:99999:00000:')
    TRIANGLE_LEFT : Any ## <class 'Image'> = Image('90000:99000:90900:90090:99999:')
    TSHIRT : Any ## <class 'Image'> = Image('99099:99999:09990:09990:09990:')
    UMBRELLA : Any ## <class 'Image'> = Image('09990:99999:00900:90900:09900:')
    XMAS : Any ## <class 'Image'> = Image('00900:09990:00900:09990:99999:')
    YES : Any ## <class 'Image'> = Image('00000:00009:00090:90900:09000:')
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

LEFT = 5 # type: int
RIGHT = 2 # type: int
TOP = 0 # type: int

class USB_VCP():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    CTS = 2 # type: int
    RTS = 1 # type: int
    def any(self, *args, **kwargs) -> Any:
        """"""

    def callback(self, *args, **kwargs) -> Any:
        """"""

    def close(self, *args, **kwargs) -> Any:
        """"""

    def init(self, *args, **kwargs) -> Any:
        """"""

    def isconnected(self, *args, **kwargs) -> Any:
        """"""

    def read(self, *args, **kwargs) -> Any:
        """"""

    def readinto(self, *args, **kwargs) -> Any:
        """"""

    def readline(self, *args, **kwargs) -> Any:
        """"""

    def readlines(self, *args, **kwargs) -> Any:
        """"""

    def recv(self, *args, **kwargs) -> Any:
        """"""

    def send(self, *args, **kwargs) -> Any:
        """"""

    def setinterrupt(self, *args, **kwargs) -> Any:
        """"""

    def write(self, *args, **kwargs) -> Any:
        """"""

battery : Any ## <class 'Battery'> = Battery class
bluetooth : Any ## <class 'bluetooth'> = <bluetooth>

class button():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    center : Any ## <class ''> = center
    connect : Any ## <class ''> = connect
    left : Any ## <class ''> = left
    right : Any ## <class ''> = right
config = {} # type: dict
display : Any ## <class 'Display'> = <Display>
def file_transfer(*args, **kwargs) -> Any:
    """"""

def info(*args, **kwargs) -> Any:
    """"""

def led(*args, **kwargs) -> Any:
    """"""

motion : Any ## <class 'Motion'> = Motion()

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
def power_off(*args, **kwargs) -> Any:
    """"""

def repl_restart(*args, **kwargs) -> Any:
    """"""

def reset(*args, **kwargs) -> Any:
    """"""

sound : Any ## <class 'Sound'> = Sound()
def status(*args, **kwargs) -> Any:
    """"""

supervision : Any ## <class 'supervision'> = <supervision>
def temperature(*args, **kwargs) -> Any:
    """"""


class _Button():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    @classmethod
    def callback(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def is_pressed(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def on_change(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def presses(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def was_pressed(cls, *args, **kwargs) -> Any:
        """"""


class _Device():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    FORMAT_PCT = 1 # type: int
    FORMAT_RAW = 0 # type: int
    FORMAT_SI = 2 # type: int
    @classmethod
    def get(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def mode(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def pwm(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def write_direct(cls, *args, **kwargs) -> Any:
        """"""


class _Motor():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    BUSY_MODE = 0 # type: int
    BUSY_MOTOR = 1 # type: int
    EVENT_COMPLETED = 0 # type: int
    EVENT_INTERRUPTED = 1 # type: int
    FORMAT_PCT = 1 # type: int
    FORMAT_RAW = 0 # type: int
    FORMAT_SI = 2 # type: int
    PID_POSITION = 1 # type: int
    PID_SPEED = 0 # type: int
    STOP_BRAKE = 1 # type: int
    STOP_FLOAT = 0 # type: int
    STOP_HOLD = 2 # type: int
    @classmethod
    def brake(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def busy(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def callback(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def default(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def float(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def get(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def hold(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def invert(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def mode(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def pair(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def pid(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def preset(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def pwm(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def run_at_speed(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def run_for_degrees(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def run_for_time(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def run_to_position(cls, *args, **kwargs) -> Any:
        """"""


class _MotorPair():
    @classmethod
    def brake(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def callback(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def default(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def float(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def hold(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def id(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def pid(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def preset(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def primary(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def pwm(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def run_at_speed(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def run_for_degrees(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def run_for_time(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def run_to_position(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def secondary(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def unpair(cls, *args, **kwargs) -> Any:
        """"""


class _Pin():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    @classmethod
    def direction(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def value(cls, *args, **kwargs) -> Any:
        """"""


class _Port():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    @classmethod
    def callback(cls, *args, **kwargs) -> Any:
        """"""

    device : Any ## <class 'NoneType'> = None
    @classmethod
    def info(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def mode(cls, *args, **kwargs) -> Any:
        """"""

    motor : Any ## <class 'NoneType'> = None
    p5 : Any ## <class 'Port'> = Port(E)
    p6 : Any ## <class 'Port'> = Port(E)
    @classmethod
    def pwm(cls, *args, **kwargs) -> Any:
        """"""


class _battery():
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
    @classmethod
    def capacity_left(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def charger_detect(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def current(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def info(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def temperature(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def voltage(cls, *args, **kwargs) -> Any:
        """"""


class _bluetooth():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    @classmethod
    def discoverable(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def forget(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def info(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def lwp_advertise(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def lwp_bypass(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def lwp_monitor(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def rfcomm_connect(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def rfcomm_disconnect(cls, *args, **kwargs) -> Any:
        """"""


class _button():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    center : Any ## <class ''> = center
    connect : Any ## <class ''> = connect
    left : Any ## <class ''> = left
    right : Any ## <class ''> = right

class _display():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    @classmethod
    def align(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def callback(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def clear(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def invert(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def pixel(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def rotation(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def show(cls, *args, **kwargs) -> Any:
        """"""


class _motion():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    DOUBLETAPPED = 1 # type: int
    FREEFALL = 3 # type: int
    SHAKE = 2 # type: int
    TAPPED = 0 # type: int
    @classmethod
    def accelerometer(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def align_to_model(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def gesture(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def gyroscope(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def orientation(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def yaw_pitch_roll(cls, *args, **kwargs) -> Any:
        """"""


class _port():
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

class _sound():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    SOUND_SAWTOOTH = 3 # type: int
    SOUND_SIN = 0 # type: int
    SOUND_SQUARE = 1 # type: int
    SOUND_TRIANGLE = 2 # type: int
    @classmethod
    def beep(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def callback(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def play(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def volume(cls, *args, **kwargs) -> Any:
        """"""


class _supervision():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    @classmethod
    def callback(cls, *args, **kwargs) -> Any:
        """"""

    @classmethod
    def info(cls, *args, **kwargs) -> Any:
        """"""

