"""
The higher-level API for Mindstorms Robot Inventor hub.
"""

from _api import (
    app,
    button,
    colorsensor,
    distancesensor,
    forcesensor,
    large_technic_hub,
    lightmatrix,
    motionsensor,
    motor,
    motorpair,
    speaker,
    statuslight,
    util,
)
from _api.app import App
from _api.button import Button
from _api.colorsensor import ColorSensor
from _api.distancesensor import DistanceSensor
from _api.forcesensor import ForceSensor
from _api.lightmatrix import LightMatrix
from _api.motionsensor import MotionSensor
from _api.motor import Motor
from _api.motorpair import MotorPair
from _api.speaker import Speaker
from _api.statuslight import StatusLight

class MSHub(large_technic_hub.LargeTechnicHub):
    def __init__(self) -> None:
        """"""
