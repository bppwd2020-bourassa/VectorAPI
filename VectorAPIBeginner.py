import anki_vector
from anki_vector.behavior import MIN_HEAD_ANGLE, MAX_HEAD_ANGLE
from anki_vector.util import degrees
from anki_vector.util import distance_mm, speed_mmps
import time

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
		Returns true for status that was passed (most wont be used) (1-17)

		1. Motors: True if motors are moving
		2. Wheels: True if wheels are moving
		3. Animating: True if doing an animation
		4. Held: True if being held
		5. Button Press: True if the button is pressed
		6. Carrying Block: True if carrying block
		7. Charging: True if charging
		8. Detected Cliff: True if on cliff
		9. Docking to marker: True if Vector has seen a marker and is actively heading toward it (for example his charger or cube)
		10. Falling: True if falling
		11. Head in pos: True if Vector’s head is in the desired position (False if still trying to move there)
		12. Calm power mode: True if Vector is in calm power mode. Calm power mode is generally when Vector is sleeping or charging.
		13. Lift in pos: True if Vector’s arm is in the desired position (False if still trying to move it there)
		14. On charger: True if on charger
		15. Pathing: True if traversing a path
		16. Picked up: True if currently picked up
		17. Moving: True if Vector is in motion. This includes any of his motors (head, arm, wheels/tracks) and if he is being lifted, carried, or falling.
		"""
		if statusCheck == 1:
			return self.conn.status.are_motors_moving
		if statusCheck == 2:
			return self.conn.status.are_wheels_moving
		if statusCheck == 3:
			return self.conn.status.is_animating
		if statusCheck == 4:
			return self.conn.status.is_being_held
		if statusCheck == 5:
			return self.conn.status.is_button_pressed
		if statusCheck == 6:
			return self.conn.status.is_carrying_block
		if statusCheck == 7:
			return self.conn.status.is_charging
		if statusCheck == 8:
			return self.conn.status.is_cliff_detected
		if statusCheck == 9:
			return self.conn.status.is_docking_to_marker
		if statusCheck == 10:
			return self.conn.status.is_falling
		if statusCheck == 11:
			return self.conn.status.is_head_in_pos
		if statusCheck == 12:
			return self.conn.status.is_in_calm_power_mode
		if statusCheck == 13:
			return self.conn.status.is_lift_in_pos
		if statusCheck == 14:
			return self.conn.status.is_on_charger
		if statusCheck == 15:
			return self.conn.status.is_pathing
		if statusCheck == 16:
			return self.conn.status.is_picked_up
		if statusCheck == 17:
			return self.conn.status.is_robot_moving
