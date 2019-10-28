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

vector.streamWAVFile('Pacman-death-sound.wav', 50)

vector.openCamera(100, True)

"""
Take out of comments if you want to test otherwise don't it'll interrupt other code
"""
"""
while True:
	if vector.getStatus(5):
		vector.talk("Hi")
"""
vector.talk("Done")
