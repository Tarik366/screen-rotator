import rotatescreen
import sys
import re

rte = rotatescreen.get_primary_display()

cr = rte.current_orientation
if cr == 0:
    rte.set_portrait()
else:
    rte.set_landscape()

    
