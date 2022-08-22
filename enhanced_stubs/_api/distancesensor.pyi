from typing import Final, Optional


class DistanceSensor:
    CM:Final[str] = "cm"
    IN:Final[str] = "in"
    PERCENT:Final[str] = "%"

    def __init__(self, port: str) -> None:
        """"""

    def get_distance_cm(self, short_range: bool = False) -> Optional[int]:
        """"""

    def get_distance_inches(self, short_range: bool = False) -> Optional[int]:
        """"""

    def get_distance_percentage(self, short_range: bool = False) -> Optional[int]:
        """"""

    def wait_for_distance_farther_than(self, distance:float, unit:str="cm", short_range: bool = False) -> None:
        """"""
    def wait_for_distance_closer_than(self, distance:float, unit:str="cm", short_range: bool = False) -> None:
        """"""

    def light_up_all(self, brightness:int=100) -> None:
        """"""
    def light_up(self, right_top:int=100, left_top:int=100, right_bottom:int=100, left_bottom:int=100) -> None:
        """"""
