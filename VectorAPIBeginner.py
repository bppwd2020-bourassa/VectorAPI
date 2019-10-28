import anki_vector
from anki_vector.behavior import MIN_HEAD_ANGLE, MAX_HEAD_ANGLE
from anki_vector.util import degrees
from anki_vector.util import distance_mm, speed_mmps
import time
from enum import Enum, auto

class RobotStatus(Enum):
	motors_moving = auto()
	wheels_moving = auto()
	is_animating = auto()
	being_held = auto()
	button_pressed = auto()
	carrying_block = auto()
	is_charging = auto()
	cliff_detected = auto()
	docking_to_marker = auto()
	is_falling = auto()
	head_in_pos = auto()
	calm_power_mode = auto()
	lift_in_pos = auto()
	on_charger = auto()
	is_pathing = auto()
	is_picked_up = auto()
	is_moving = auto()

class VectorOBJ:

	def __init__(self, serial):
		"""
		Constructor for the vector obj
		"""
		self.conn = anki_vector.Robot(serial)

	def connect(self):
		"""
		Connects to vector initialized
		"""
		self.conn.connect()

	def forward(self, distance, speed):
		"""
		Makes vector go forward
		"""
		if speed.upper() == "FAST":
			self.conn.behavior.drive_straight(distance_mm(distance), speed_mmps(500))
		elif speed.upper() == "SLOW":
			self.conn.behavior.drive_straight(distance_mm(distance), speed_mmps(150))

	def backward(self, distance, speed):
		"""
		Makes vector go backward
		"""
		if speed.upper() == "FAST":
			self.conn.behavior.drive_straight(distance_mm(-distance), speed_mmps(500))
		elif speed.upper() == "SLOW":
			self.conn.behavior.drive_straight(distance_mm(-distance), speed_mmps(150))

	def right(self, angle):
		"""
		Turns vector right
		"""
		self.conn.behavior.turn_in_place(degrees(angle))

	def left(self, angle):
		"""
		Turns vector left
		"""
		self.conn.behavior.turn_in_place(degrees(-angle))

	def raiseArm(self):
		"""
		Raises arm
		"""
		self.conn.motors.set_lift_motor(5.0)
		time.sleep(2)

	def lowerArm(self):
		"""
		Lowers arm
		"""
		self.conn.motors.set_lift_motor(-5.0)
		time.sleep(2)

	def raiseHead(self):
		"""
		Raises head
		"""
		self.conn.motors.set_head_motor(5.0)

	def lowerHead(self):
		"""
		Lowers head
		"""
		self.conn.motors.set_head_motor(-5.0)

	def talk(self, text):
		"""
		Vector says the text
		"""
		self.conn.behavior.say_text(text)

	def objectDetected(self):
		"""
		Detects object
		"""
		return self.conn.proximity.last_sensor_reading.found_object

	def driveOnCharger(self):
		"""
		Method for driving on charger
		"""
		self.conn.behavior.drive_on_charger()

	def driveOffCharger(self):
		"""
		Method for driving off charger
		"""
		self.conn.behavior.drive_off_charger()

	def dockCube(self):
		"""
		Docks to connected cube
		"""
		print("Connecting")
		self.conn.world.connect_cube()
		if self.conn.world.connected_light_cube:
			self.conn.behavior.dock_with_cube(self.conn.world.connected_light_cube)

	def isTouch(self):
		"""
		Outputs true if touched
		"""
		touch_data = self.conn.touch.last_sensor_reading
		if touch_data is not None:
			is_being_touched = touch_data.is_being_touched
			if is_being_touched:
				return True

	def openCamera(self, length, count):
		"""
		Displays camera for length (sec) counts down for how much longer you have
		"""
		while (length > 0):
			self.conn.vision.enable_face_detection(detect_faces=True)
			self.conn.vision.enable_custom_object_detection(detect_custom_objects=True)
			self.conn.vision.enable_display_camera_feed_on_face(display_camera_feed_on_face=True)
			if count:
				self.conn.behavior.say_text(str(length))
			length = length - 1

	def streamWAVFile(self, path, volume):
		"""
		Stremas the wav file from specified path with specified volume(0-100)
		"""
		self.conn.audio.stream_wav_file(path, volume)

	def getStatus(self, statusCheck):
		"""
		Returns true for status that was passed (most wont be used)  RobotStatus.(1-17)

		1. motors_moving: True if motors are moving
		2. wheels_moving: True if wheels are moving
		3. is_animating: True if doing an animation
		4. being_held: True if being held
		5. button_press: True if the button is pressed
		6. carrying_block: True if carrying block
		7. is_charging: True if charging
		8. cliff_detected: True if on cliff
		9. docking_to_marker: True if Vector has seen a marker and is actively heading toward it (for example his charger or cube)
		10. is_falling: True if falling
		11. head_in_pos: True if Vector’s head is in the desired position (False if still trying to move there)
		12. calm_power_mode: True if Vector is in calm power mode. Calm power mode is generally when Vector is sleeping or charging.
		13. lift_in_pos: True if Vector’s arm is in the desired position (False if still trying to move it there)
		14. on_charger: True if on charger
		15. is_pathing: True if traversing a path
		16. is_picked_up: True if currently picked up
		17. is_moving: True if Vector is in motion. This includes any of his motors (head, arm, wheels/tracks) and if he is being lifted, carried, or falling.
		"""

		if statusCheck == RobotStatus.motors_moving:
			return self.conn.status.are_motors_moving
		if statusCheck == RobotStatus.wheels_moving:
			return self.conn.status.are_wheels_moving
		if statusCheck == RobotStatus.is_animating:
			return self.conn.status.is_animating
		if statusCheck == RobotStatus.being_held:
			return self.conn.status.is_being_held
		if statusCheck == RobotStatus.button_pressed:
			return self.conn.status.is_button_pressed
		if statusCheck == RobotStatus.carrying_block:
			return self.conn.status.is_carrying_block
		if statusCheck == RobotStatus.is_charging:
			return self.conn.status.is_charging
		if statusCheck == RobotStatus.cliff_detected:
			return self.conn.status.is_cliff_detected
		if statusCheck == RobotStatus.docking_to_marker:
			return self.conn.status.is_docking_to_marker
		if statusCheck == RobotStatus.is_falling:
			return self.conn.status.is_falling
		if statusCheck == RobotStatus.head_in_pos:
			return self.conn.status.is_head_in_pos
		if statusCheck == RobotStatus.calm_power_mode:
			return self.conn.status.is_in_calm_power_mode
		if statusCheck == RobotStatus.lift_in_pos:
			return self.conn.status.is_lift_in_pos
		if statusCheck == RobotStatus.on_charger:
			return self.conn.status.is_on_charger
		if statusCheck == RobotStatus.is_pathing:
			return self.conn.status.is_pathing
		if statusCheck == RobotStatus.is_picked_up:
			return self.conn.status.is_picked_up
		if statusCheck == RobotStatus.is_moving:
			return self.conn.status.is_robot_moving
