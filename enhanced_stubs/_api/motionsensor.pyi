from typing import Any, Final


class MotionSensor:
    BACK:str = "back"
    DOUBLE_TAPPED:str = "doubletapped"
    DOWN:str = "down"
    FALLING:str = "falling"
    FRONT:str = "front"
    LEFT_SIDE:str = "leftside"
    RIGHT_SIDE:str = "rightside"
    SHAKEN:str = "shaken"
    TAPPED:str = "tapped"
    UP:str = "up"

    def was_gesture(self, gesture:str) -> bool:
        """
        gesture: one of "shaken", "tapped", "doubletapped", "falling"
        """

    def wait_for_new_gesture(self) -> str:
        """"""

    def wait_for_new_orientation(self) -> str:
        """"""


    def get_orientation(self) -> str:
        """"""
    def get_gesture(self) -> str:
        """"""
    def get_pitch_angle(self) -> int:
        """"""
    def get_roll_angle(self) -> int:
        """"""
    def get_yaw_angle(self) -> int:
        """"""

    def reset_yaw_angle(self) -> None:
        """"""

    def align_to_model(self, top_face:str, front_face: str) -> None:
        """
        top_face/front_face: one of "front", "up", "rightside", "back", "down", "leftside"
        """
