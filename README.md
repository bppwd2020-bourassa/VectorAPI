#VectorAPI

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
     |  animation(self, anim_name)
     |      Plays the animation given
     |      for the list of animations run anim_names.py
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
     |      1. motors_moving: True if motors are moving
     |      2. wheels_moving: True if wheels are moving
     |      3. is_animating: True if doing an animation
     |      4. being_held: True if being held
     |      5. button_press: True if the button is pressed
     |      6. carrying_block: True if carrying block
     |      7. is_charging: True if charging
     |      8. cliff_detected: True if on cliff
     |      9. docking_to_marker: True if Vector has seen a marker and is actively heading toward it (for example his charger or cube)
     |      10. is_falling: True if falling
     |      11. head_in_pos: True if VectorÆs head is in the desired position (False if still trying to move there)
     |      12. calm_power_mode: True if Vector is in calm power mode. Calm power mode is generally when Vector is sleeping or charging.
     |      13. lift_in_pos: True if VectorÆs arm is in the desired position (False if still trying to move it there)
     |      14. on_charger: True if on charger
     |      15. is_pathing: True if traversing a path
     |      16. is_picked_up: True if currently picked up
     |      17. is_moving: True if Vector is in motion. This includes any of his motors (head, arm, wheels/tracks) and if he is being lifted, carried, or falling.
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
