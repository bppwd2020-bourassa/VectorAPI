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

	def animation(self, anim_name):
		"""
		Plays the animation given
		for the list of animations
		"""
		self.conn.anim.play_animation(anim_name)

	def pick_up_cube(self):
		"""
		Automatically picks up cube (line him up with cube)
		"""
		print("Connecting")
		self.conn.world.connect_cube()
		if self.conn.world.connected_light_cube:
			self.conn.behavior.dock_with_cube(self.conn.world.connected_light_cube)
			self.conn.motors.set_lift_motor(5.0)

	def getStatus(self, statusCheck):
		"""
		Returns true for status that was passed (most wont be used) (1-17)

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

		status = {'motors_moving': self.conn.status.are_motors_moving, 'wheels_moving': self.conn.status.are_wheels_moving, 'is_animating': self.conn.status.is_animating, 'being_held':self.conn.status.is_being_held, 'button_pressed': self.conn.status.is_button_pressed, 'carrying_block': self.conn.status.is_carrying_block, 'is_charging': self.conn.status.is_charging, 'cliff_detected': self.conn.status.is_cliff_detected, 'docking_to_marker': self.conn.status.is_docking_to_marker, 'is_falling': self.conn.status.is_falling, 'head_in_pos': self.conn.status.is_head_in_pos, 'calm_power_mode': self.conn.status.is_in_calm_power_mode, 'lift_in_pos':self.conn.status.is_lift_in_pos, 'on_charger':self.conn.status.is_on_charger, 'is_pathing':self.conn.status.is_pathing, 'is_picked_up':self.conn.status.is_picked_up, 'is_moving':self.conn.status.is_robot_moving}

		return status[statusCheck]

	def stop_wheel_motors(self):
		self.conn.motors.stop_all_motors()

	def __set_wheel_motors(self, left, right):
		"""
		Sets the wheels motors
		"""
		self.conn.motors.set_wheel_motors(left, right)
