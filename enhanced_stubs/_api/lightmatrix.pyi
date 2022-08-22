from typing import List, Sequence

FACES:List[int]
ORIENTATIONS:List[str]

class LightMatrix:
    def set_pixel(self, x:int, y:int, brightness:int=100) -> None:
        """
        x, y : 0-4
        brightness: 0-100
        """
    def show_image(self, image:str, brightness:int=100) -> None:
        """
        image: one of 'ANGRY', 'ARROW_E', 'ARROW_N', 'ARROW_NE', 'ARROW_NW', 'ARROW_S', 'ARROW_SE', 'ARROW_SW', 'ARROW_W', 'ASLEEP', 'BUTTERFLY', 'CHESSBOARD', 'CLOCK1', 'CLOCK10', 'CLOCK11', 'CLOCK12', 'CLOCK2', 'CLOCK3', 'CLOCK4', 'CLOCK5', 'CLOCK6', 'CLOCK7', 'CLOCK8', 'CLOCK9', 'CONFUSED', 'COW', 'DIAMOND', 'DIAMOND_SMALL', 'DUCK', 'FABULOUS', 'GHOST', 'GIRAFFE', 'GO_DOWN', 'GO_LEFT', 'GO_RIGHT', 'GO_UP', 'HAPPY', 'HEART', 'HEART_SMALL', 'HOUSE', 'MEH', 'MUSIC_CROTCHET', 'MUSIC_QUAVER', 'MUSIC_QUAVERS', 'NO', 'PACMAN', 'PITCHFORK', 'RABBIT', 'ROLLERSKATE', 'SAD', 'SILLY', 'SKULL', 'SMILE', 'SNAKE', 'SQUARE', 'SQUARE_SMALL', 'STICKFIGURE', 'SURPRISED', 'SWORD', 'TARGET', 'TORTOISE', 'TRIANGLE', 'TRIANGLE_LEFT', 'TSHIRT', 'UMBRELLA', 'XMAS', 'YES'
        """
    def write(self, text: str) -> None:
        """"""
    def off(self) -> None:
        """"""

    def show(self, pixels:str) -> None:
        """
        Example: ``hub.light_matrix.show('99999:77777:55555:33333:11111')``
        """
    def play_animation(self, animation:Sequence[str], fps: float=2.5, effect:str="direct",
                       clear:bool=False) -> None:
        """
        fps: 1-20
        effect: one of "direct", "overlay", "slide right", "slide left", "fade in", "fade out"
        """

    def start_animation(self, animation:Sequence[str], fps: float=2.5, loop:bool=False, effect:str="direct",
                       clear:bool=False) -> None:
        """"""

    def set_orientation(self, orientation:str="upright") -> None:
        """
        orientation: one of "upright", "left", "upside down", "right"
        """
    def get_orientation(self) -> str:
        """"""

    def rotate(self, direction: str="clockwise") -> None:
        """
        direction: one of "clockwise", "counterclockwise"
        """


def get_current_orientation() -> str:
    """"""

def rotate_orientation(arg:str) -> None:
    """"""

def set_current_orientation(orientation:str) -> None:
    """"""
