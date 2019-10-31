import sys

sys.path.insert(1, 'C:/Users/jrb32/Desktop/VectorAPI/API Files')

from VectorAPIBeginner import *
from JoystickClass import *

joystick = Joystick()
joystick.draw()
joystick.update()
