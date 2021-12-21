import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation

# from kmk.matrix import intify_coordinate as ic


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP8,
        board.GP7,
        board.GP6,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP10,
        board.GP15,
        board.GP14,
        board.GP13,
        board.GP12,
        board.GP11,
        board.GP9,
        board.GP21,
    )

    row_pins = (board.GP20, board.GP19, board.GP18, board.GP17, board.GP16,)

    #diode_orientation = DiodeOrientation.ROWS
    diode_orientation = DiodeOrientation.COLUMNS
