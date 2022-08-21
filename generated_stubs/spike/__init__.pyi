"""
Module: 'spike' on micropython-v1.14-893-lego learning system hub
"""
# MCU: {'machine': 'LEGO Technic Large Hub with STM32F413xx', 'sysname': 'LEGO Technic Large Hub', 'platform': 'LEGO Learning System Hub', 'nodename': 'LEGO Learning System Hub', 'ver': 'v1.14-893', 'release': '1.14.0', 'name': 'micropython', 'family': 'micropython', 'port': 'LEGO Learning System Hub', 'version': '1.14.0', 'mpy': 517, 'build': '893'}
# Stubber: 1.7.2
from typing import Any


class App():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def play_sound(self, *args, **kwargs) -> Any:
        """"""

    def start_sound(self, *args, **kwargs) -> Any:
        """"""

    def stop_sound(self, *args, **kwargs) -> Any:
        """"""


class Button():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def is_pressed(self, *args, **kwargs) -> Any:
        """"""

    def is_released(self, *args, **kwargs) -> Any:
        """"""

    def wait_until_pressed(self, *args, **kwargs) -> Any:
        """"""

    def wait_until_released(self, *args, **kwargs) -> Any:
        """"""

    def was_pressed(self, *args, **kwargs) -> Any:
        """"""


class ColorSensor():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def get_ambient_light(self, *args, **kwargs) -> Any:
        """"""

    def get_blue(self, *args, **kwargs) -> Any:
        """"""

    def get_color(self, *args, **kwargs) -> Any:
        """"""

    def get_green(self, *args, **kwargs) -> Any:
        """"""

    def get_red(self, *args, **kwargs) -> Any:
        """"""

    def get_reflected_light(self, *args, **kwargs) -> Any:
        """"""

    def get_rgb_intensity(self, *args, **kwargs) -> Any:
        """"""

    def light_up(self, *args, **kwargs) -> Any:
        """"""

    def light_up_all(self, *args, **kwargs) -> Any:
        """"""

    def wait_for_new_color(self, *args, **kwargs) -> Any:
        """"""

    def wait_until_color(self, *args, **kwargs) -> Any:
        """"""


class DistanceSensor():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    CM = 'cm' # type: str
    IN = 'in' # type: str
    PERCENT = '%' # type: str
    def get_distance_cm(self, *args, **kwargs) -> Any:
        """"""

    def get_distance_inches(self, *args, **kwargs) -> Any:
        """"""

    def get_distance_percentage(self, *args, **kwargs) -> Any:
        """"""

    def light_up(self, *args, **kwargs) -> Any:
        """"""

    def light_up_all(self, *args, **kwargs) -> Any:
        """"""

    def wait_for_distance_closer_than(self, *args, **kwargs) -> Any:
        """"""

    def wait_for_distance_farther_than(self, *args, **kwargs) -> Any:
        """"""


class ForceSensor():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def get_force_newton(self, *args, **kwargs) -> Any:
        """"""

    def get_force_percentage(self, *args, **kwargs) -> Any:
        """"""

    def is_pressed(self, *args, **kwargs) -> Any:
        """"""

    def wait_until_pressed(self, *args, **kwargs) -> Any:
        """"""

    def wait_until_released(self, *args, **kwargs) -> Any:
        """"""


class LightMatrix():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def get_orientation(self, *args, **kwargs) -> Any:
        """"""

    def off(self, *args, **kwargs) -> Any:
        """"""

    def play_animation(self, *args, **kwargs) -> Any:
        """"""

    def rotate(self, *args, **kwargs) -> Any:
        """"""

    def set_orientation(self, *args, **kwargs) -> Any:
        """"""

    def set_pixel(self, *args, **kwargs) -> Any:
        """"""

    def show(self, *args, **kwargs) -> Any:
        """"""

    def show_image(self, *args, **kwargs) -> Any:
        """"""

    def start_animation(self, *args, **kwargs) -> Any:
        """"""

    def write(self, *args, **kwargs) -> Any:
        """"""


class MotionSensor():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    BACK = 'back' # type: str
    DOUBLE_TAPPED = 'doubletapped' # type: str
    DOWN = 'down' # type: str
    FALLING = 'falling' # type: str
    FRONT = 'front' # type: str
    LEFT_SIDE = 'leftside' # type: str
    RIGHT_SIDE = 'rightside' # type: str
    SHAKEN = 'shaken' # type: str
    TAPPED = 'tapped' # type: str
    UP = 'up' # type: str
    def align_to_model(self, *args, **kwargs) -> Any:
        """"""

    def get_gesture(self, *args, **kwargs) -> Any:
        """"""

    def get_orientation(self, *args, **kwargs) -> Any:
        """"""

    def get_pitch_angle(self, *args, **kwargs) -> Any:
        """"""

    def get_roll_angle(self, *args, **kwargs) -> Any:
        """"""

    def get_yaw_angle(self, *args, **kwargs) -> Any:
        """"""

    def reset_yaw_angle(self, *args, **kwargs) -> Any:
        """"""

    def wait_for_new_gesture(self, *args, **kwargs) -> Any:
        """"""

    def wait_for_new_orientation(self, *args, **kwargs) -> Any:
        """"""

    def was_gesture(self, *args, **kwargs) -> Any:
        """"""


class Motor():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    BRAKE = 'brake' # type: str
    COAST = 'coast' # type: str
    HOLD = 'hold' # type: str
    def get_default_speed(self, *args, **kwargs) -> Any:
        """"""

    def get_degrees_counted(self, *args, **kwargs) -> Any:
        """"""

    def get_position(self, *args, **kwargs) -> Any:
        """"""

    def get_speed(self, *args, **kwargs) -> Any:
        """"""

    def run_for_degrees(self, *args, **kwargs) -> Any:
        """"""

    def run_for_rotations(self, *args, **kwargs) -> Any:
        """"""

    def run_for_seconds(self, *args, **kwargs) -> Any:
        """"""

    def run_to_degrees_counted(self, *args, **kwargs) -> Any:
        """"""

    def run_to_position(self, *args, **kwargs) -> Any:
        """"""

    def set_default_speed(self, *args, **kwargs) -> Any:
        """"""

    def set_degrees_counted(self, *args, **kwargs) -> Any:
        """"""

    def set_stall_detection(self, *args, **kwargs) -> Any:
        """"""

    def set_stop_action(self, *args, **kwargs) -> Any:
        """"""

    def start(self, *args, **kwargs) -> Any:
        """"""

    def start_at_power(self, *args, **kwargs) -> Any:
        """"""

    def stop(self, *args, **kwargs) -> Any:
        """"""

    def was_interrupted(self, *args, **kwargs) -> Any:
        """"""

    def was_stalled(self, *args, **kwargs) -> Any:
        """"""


class MotorPair():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    BRAKE = 'brake' # type: str
    CM = 'cm' # type: str
    COAST = 'coast' # type: str
    DEGREES = 'degrees' # type: str
    HOLD = 'hold' # type: str
    IN = 'in' # type: str
    ROTATIONS = 'rotations' # type: str
    SECONDS = 'seconds' # type: str
    def get_default_speed(self, *args, **kwargs) -> Any:
        """"""

    def move(self, *args, **kwargs) -> Any:
        """"""

    def move_tank(self, *args, **kwargs) -> Any:
        """"""

    def set_default_speed(self, *args, **kwargs) -> Any:
        """"""

    def set_motor_rotation(self, *args, **kwargs) -> Any:
        """"""

    def set_stop_action(self, *args, **kwargs) -> Any:
        """"""

    def start(self, *args, **kwargs) -> Any:
        """"""

    def start_at_power(self, *args, **kwargs) -> Any:
        """"""

    def start_tank(self, *args, **kwargs) -> Any:
        """"""

    def start_tank_at_power(self, *args, **kwargs) -> Any:
        """"""

    def stop(self, *args, **kwargs) -> Any:
        """"""

    def was_interrupted(self, *args, **kwargs) -> Any:
        """"""


class PrimeHub():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    PORT_A = 'A' # type: str
    PORT_B = 'B' # type: str
    PORT_C = 'C' # type: str
    PORT_D = 'D' # type: str
    PORT_E = 'E' # type: str
    PORT_F = 'F' # type: str
    left_button : Any ## <class 'property'> = <property>
    light_matrix : Any ## <class 'property'> = <property>
    motion_sensor : Any ## <class 'property'> = <property>
    right_button : Any ## <class 'property'> = <property>
    speaker : Any ## <class 'property'> = <property>
    status_light : Any ## <class 'property'> = <property>

class Speaker():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def beep(self, *args, **kwargs) -> Any:
        """"""

    def get_volume(self, *args, **kwargs) -> Any:
        """"""

    def play_sound(self, *args, **kwargs) -> Any:
        """"""

    def set_volume(self, *args, **kwargs) -> Any:
        """"""

    def start_beep(self, *args, **kwargs) -> Any:
        """"""

    def start_sound(self, *args, **kwargs) -> Any:
        """"""

    def stop(self, *args, **kwargs) -> Any:
        """"""


class StatusLight():
    def __init__(self, *argv, **kwargs) -> None:
        """"""

    def off(self, *args, **kwargs) -> Any:
        """"""

    def on(self, *args, **kwargs) -> Any:
        """"""

