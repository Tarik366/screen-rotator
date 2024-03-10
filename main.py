import rotatescreen
import sys
import re

rte = rotatescreen.get_primary_display()

def change_rotation():
    cr = rte.current_orientation
    if cr == 0:
        rte.set_portrait()
    else:
        rte.set_landscape()

import keyboard  # using module keyboard


keyboard.add_hotkey('win + page up', change_rotation)  # create hotkey
keyboard.wait('')
