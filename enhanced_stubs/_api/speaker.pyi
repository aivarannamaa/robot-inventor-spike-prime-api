from typing import Any, Optional, List


class Speaker:
    def beep(self, note: int=60, seconds: float=0.2, volume:Optional[int]=None) -> None:
        """
        note: the MIDI note number (44-123)
        volume: 1-100. None means use current volume
        """

    def start_beep(self, note: int=60, volume:Optional[int]=None) -> None:
        """
        Plays until stop or another beep.
        """
    def stop(self) -> None:
        """"""
    def play_sound(self, name: str, volume:Optional[int]=None) -> None:
        """
        name: one of '1234', 'Activate', 'Affirmative', 'Bowling', 'Brick Eating', 'Celebrate', 'Chuckle', 'Countdown', 'Countdown Tick', 'Damage', 'Deactivate', 'Delivery', 'Dizzy', 'Error', 'Explosion', 'Exterminate', 'Fire', 'Goal', 'Goodbye', 'Grab', 'Hammer', 'Hello', 'Hi', 'Hi 5', 'Hit', 'Horn', 'Humming', 'Hydraulics Down', 'Hydraulics Up', 'Initialize', 'Kick', 'Laser', 'Laugh', 'Like', 'Mission Accomplished', 'No', 'Ouch', 'Ping', 'Play', 'Punch', 'Reverse', 'Revving', 'Sad', 'Scanning', 'Scared', 'Seek and Destroy', 'Shake', 'Shooting', 'Shut Down', 'Slam Dunk', 'Strike', 'Success Chime', 'Tadaa', 'Target Acquired', 'Target Destroyed', 'Whirl', 'Wow', 'Yes', 'Yipee', 'Yuck'

        See ``os.listdir("/extra_files") for all sounds``
        """
    def start_sound(self, name: str, volume:Optional[int]=None) -> None:
        """"""
    def get_volume(self) -> int:
        """"""
    def set_volume(self, volume:int=100) -> None:
        """"""

class SpeakerSoundProvider:
    def __init__(self) -> None:
        """"""
    def get_canonical_name(self, name:str) -> str:
        """
        Returns path of the corresponding sound file
        """
    def get_sound_files(self) -> List[str]:
        """
        Returns sequence of sound names.
        """
