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
     |  getStatus(self, statusCheck)
     |      Returns true for status that was passed (most wont be used) (1-17)
     |
     |      1. Motors: True if motors are moving
     |      2. Wheels: True if wheels are moving
     |      3. Animating: True if doing an animation
     |      4. Held: True if being held
     |      5. Button Press: True if the button is pressed
     |      6. Carrying Block: True if carrying block
     |      7. Charging: True if charging
     |      8. Detected Cliff: True if on cliff
     |      9. Docking to marker: True if Vector has seen a marker and is actively heading toward it (for example his charger or cube)
     |      10. Falling: True if falling
     |      11. Head in pos: True if VectorÆs head is in the desired position (False if still trying to move there)
     |      12. Calm power mode: True if Vector is in calm power mode. Calm power mode is generally when Vector is sleeping or charging.
     |      13. Lift in pos: True if VectorÆs arm is in the desired position (False if still trying to move it there)
     |      14. On charger: True if on charger
     |      15. Pathing: True if traversing a path
     |      16. Picked up: True if currently picked up
     |      17. Moving: True if Vector is in motion. This includes any of his motors (head, arm, wheels/tracks) and if he is being lifted, carried, or falling.
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
