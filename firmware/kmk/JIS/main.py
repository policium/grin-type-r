from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
import kmk.extensions.keymap_extras.keymap_jp

keyboard = KMKKeyboard()
layers = Layers()
keyboard.modules = [layers,]


# ------------------User level config variables ---------------------------------------
#keyboard.unicode_mode = UnicodeMode.LINUX
keyboard.tap_time = 250

keyboard.debug_enabled = False

_______ = KC.TRNS
XXXXXXX = KC.NO

# ---------------------- Keymap ---------------------------------------------------------

keyboard.keymap = [
    [  # Default
        KC.ESC,    KC.N1,     KC.N2,     KC.N3,     KC.N4,     KC.N5,     KC.N6,     KC.N7,     KC.N8,     KC.N9,     KC.N0,     KC.MINS,   KC.CIRC,   KC.INT3,   KC.BSPC,
        KC.TAB,    KC.Q,      KC.W,      KC.E,      KC.R,      KC.T,      KC.Y,      KC.U,      KC.I,      KC.O,      KC.P,      KC.AT,     KC.LBRC,   KC.ENTER,  KC.PGUP,
        KC.CAPS,   KC.A,      KC.S,      KC.D,      KC.F,      KC.G,      KC.H,      KC.J,      KC.K,      KC.L,      KC.SCLN,   KC.COLN,   KC.RBRC,   XXXXXXX,   KC.PGDN,
        KC.LSFT,   XXXXXXX,   KC.Z,      KC.X,      KC.C,      KC.V,      KC.B,      KC.N,      KC.M,      KC.COMM,   KC.DOT,    KC.SLSH,   KC.BSLS,   KC.RSFT,   KC.DEL,
        KC.LCTL,   KC.LGUI,   KC.LALT,   XXXXXXX,   KC.LT(1, KC.LANG2),   XXXXXXX,   KC.SPC,    XXXXXXX,   KC.LT(1, KC.LANG1),   KC.APP,    KC.RCTL,    KC.LEFT,   KC.DOWN,   KC.UP,     KC.RIGHT,
    ],
    [  # Function
        KC.GRV,    KC.F1,     KC.F2,     KC.F3,     KC.F4,     KC.F5,     KC.F6,     KC.F7,     KC.F8,     KC.F9,     KC.F10,    KC.F11,    KC.F12,    XXXXXXX,   XXXXXXX,
        XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   KC.PSCR,
        XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   KC.PAUSE,
        _______,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   _______,   KC.INSERT,
        _______,   _______,   _______,   XXXXXXX,   _______,   XXXXXXX,   XXXXXXX,   XXXXXXX,   _______,   _______,   _______,   KC.HOME,   KC.PGDN,   KC.PGUP,   KC.END,
    ],
]

if __name__ == '__main__':
    keyboard.go()
