"""
Module: 'spike' on micropython-v1.14-893-lego learning system hub
"""
# MCU: {'machine': 'LEGO Technic Large Hub with STM32F413xx', 'sysname': 'LEGO Technic Large Hub', 'platform': 'LEGO Learning System Hub', 'nodename': 'LEGO Learning System Hub', 'ver': 'v1.14-893', 'release': '1.14.0', 'name': 'micropython', 'family': 'micropython', 'port': 'LEGO Learning System Hub', 'version': '1.14.0', 'mpy': 517, 'build': '893'}
# Stubber: 1.7.2

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

from _api import app, button, colorsensor, distancesensor, forcesensor, lightmatrix, \
    motionsensor, motor, motorpair, speaker, statuslight, util, large_technic_hub

class PrimeHub(large_technic_hub.LargeTechnicHub):
    def __init__(self, *argv, **kwargs) -> None:
        """"""
