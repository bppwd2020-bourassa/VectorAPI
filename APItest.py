from VectorAPIBeginner import *

"""
This is a test file to play with the api, I suggest testing using this first
"""

vector = VectorOBJ("00406214")
vector.connect()

vector.right(90)
vector.left(90)

vector.forward(100, "slow")
vector.backward(100, "Fast")

vector.dockCube()

vector.raiseArm()
vector.lowerArm()

if not vector.detectCliff():
	vector.talk("Not on cliff")
if vector.detectCliff():
	vector.talk("Im on a cliff")


if vector.isTouch():
	vector.talk("Im being touched")

vector.objectDetected()

vector.talk("Done")