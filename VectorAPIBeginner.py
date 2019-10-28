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

	def detectCliff(self):
		"""
		Returns true if hanging over a cliff
		"""
		return(self.conn.status.is_cliff_detected)

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
