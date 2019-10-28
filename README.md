# VectorAPI

NAME
    VectorAPIBeginner

CLASSES
    builtins.object
        VectorOBJ

    class VectorOBJ(builtins.object)
     |  VectorOBJ(serial)
     |
     |  Methods defined here:
     |
     |  __init__(self, serial)
     |      Constructor for the vector obj
     |
     |  backward(self, distance, speed)
     |      Makes vector go backward
     |
     |  connect(self)
     |      Connects to vector initialized
     |
     |  detectCliff(self)
     |      Returns true if hanging over a cliff
     |
     |  dockCube(self)
     |      Docks to connected cube
     |
     |  driveOffCharger(self)
     |      Method for driving off charger
     |
     |  driveOnCharger(self)
     |      Method for driving on charger
     |
     |  forward(self, distance, speed)
     |      Makes vector go forward
     |
     |  isTouch(self)
     |      Outputs true if touched
     |
     |  left(self, angle)
     |      Turns vector left
     |
     |  lowerArm(self)
     |      Lowers arm
     |
     |  lowerHead(self)
     |      Lowers head
     |
     |  objectDetected(self)
     |      Detects object
     |
     |  openCamera(self, length, count)
     |      Displays camera for length (sec) counts down for how much longer you have
     |
     |  raiseArm(self)
     |      Raises arm
     |
     |  raiseHead(self)
     |      Raises head
     |
     |  right(self, angle)
     |      Turns vector right
     |
     |  streamWAVFile(self, path, volume)
     |      Stremas the wav file from specified path with specified volume(0-100)
     |
     |  talk(self, text)
     |      Vector says the text
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

DATA
    MAX_HEAD_ANGLE = <Angle Radians: 0.79 Degrees: 45.00>
    MIN_HEAD_ANGLE = <Angle Radians: -0.38 Degrees: -22.00>

FILE
    d:\misc\vectorapi\vectorapibeginner.py
