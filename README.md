# VectorAPI

NAME
    VectorAPIBeginner

CLASSES
    builtins.object
        VectorOBJ
    enum.Enum(builtins.object)
        RobotStatus

    class RobotStatus(enum.Enum)
     |
     |  Data and other attributes defined here:
     |
     |  being_held = <RobotStatus.being_held: 4>
     |
     |  button_pressed = <RobotStatus.button_pressed: 5>
     |
     |  calm_power_mode = <RobotStatus.calm_power_mode: 12>
     |
     |  carrying_block = <RobotStatus.carrying_block: 6>
     |
     |  cliff_detected = <RobotStatus.cliff_detected: 8>
     |
     |  docking_to_marker = <RobotStatus.docking_to_marker: 9>
     |
     |  head_in_pos = <RobotStatus.head_in_pos: 11>
     |
     |  is_animating = <RobotStatus.is_animating: 3>
     |
     |  is_charging = <RobotStatus.is_charging: 7>
     |
     |  is_falling = <RobotStatus.is_falling: 10>
     |
     |  is_moving = <RobotStatus.is_moving: 17>
     |
     |  is_pathing = <RobotStatus.is_pathing: 15>
     |
     |  is_picked_up = <RobotStatus.is_picked_up: 16>
     |
     |  lift_in_pos = <RobotStatus.lift_in_pos: 13>
     |
     |  motors_moving = <RobotStatus.motors_moving: 1>
     |
     |  on_charger = <RobotStatus.on_charger: 14>
     |
     |  wheels_moving = <RobotStatus.wheels_moving: 2>
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from enum.Enum:
     |
     |  name
     |      The name of the Enum member.
     |
     |  value
     |      The value of the Enum member.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from enum.EnumMeta:
     |
     |  __members__
     |      Returns a mapping of member name->value.
     |
     |      This mapping lists all enum members, including aliases. Note that this
     |      is a read-only view of the internal mapping.

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
     |      Returns true for status that was passed (most wont be used)  RobotStatus. one of the following:
     |
     |      motors_moving: True if motors are moving
     |      wheels_moving: True if wheels are moving
     |      is_animating: True if doing an animation
     |      being_held: True if being held
     |      button_press: True if the button is pressed
     |      carrying_block: True if carrying block
     |      is_charging: True if charging
     |      cliff_detected: True if on cliff
     |      docking_to_marker: True if Vector has seen a marker and is actively heading toward it (for example his charger or cube)
     |      is_falling: True if falling
     |      head_in_pos: True if VectorÆs head is in the desired position (False if still trying to move there)
     |      calm_power_mode: True if Vector is in calm power mode. Calm power mode is generally when Vector is sleeping or charging.
     |      lift_in_pos: True if VectorÆs arm is in the desired position (False if still trying to move it there)
     |      on_charger: True if on charger
     |      is_pathing: True if traversing a path
     |      is_picked_up: True if currently picked up
     |      is_moving: True if Vector is in motion. This includes any of his motors (head, arm, wheels/tracks) and if he is being lifted, carried, or falling.
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
