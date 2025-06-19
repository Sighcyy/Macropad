import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler




# Pins
# Here I defined which inputs were connected to which digital pins on the Microcontroller
PINS = [board.D3, board.D6, board.D8,
        board.D2, board.D5, board.D7
        board.D1, board.D4
       ]
PUSHBUTTON = board.D12
ROTA = board.D11
ROTB = board.D10
LED = board.D9




#Keyboard Main Instance
keyboard = KMKKeyboard()


# Encoder settings
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ROTA, ROTB, PUSHBUTTON, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.LALT(KC.TAB))



#Lining up the digital pins defines the values of each of the pins
keyboard.keymap = [
    [KC.Q, KC.W, KC.E,
     KC.A, KC.S, KC.D,
     KC.C, KC.V
    ]
]
                  
pixels = neopixel.NeoPixel(LED, brightness=0.2, auto_write=False)
RED = (255, 0, 0)

while True:
    pixels.fill(RED)
    pixels.show()
    time.sleep(0.5)




# Start kmk!
if __name__ == '__main__':
    keyboard.go()




