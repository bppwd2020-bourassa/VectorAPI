import anki_vector
from anki_vector.behavior import MIN_HEAD_ANGLE, MAX_HEAD_ANGLE
from anki_vector.util import degrees
from anki_vector.util import distance_mm, speed_mmps
import time

class VectorObj:

	def __init__(self, serial):
		"""
		Constructor for Vector object
		"""
		self.conn = anki_vector.Robot(serial)

	def connect(self):
		"""
		Connects to vector initialized
		"""
		self.conn.connect()

	def driveStraight(self, distanceMM, speedMMPS):
		"""
		Method for driving
		Positive for forward Negative for backward 
		"""
		self.conn.behavior.drive_straight(distance_mm(distanceMM), speed_mmps(speedMMPS))

	def setMotors(self, rightwheel, leftwheel):
		"""
		Method to set the wheel motors
		"""
		self.conn.motors.set_wheel_motors(rightwheel, leftwheel)

	def driveonCharger(self):
		"""
		Method for driving on charger
		"""
		self.conn.behavior.drive_on_charger()

	def driveoffCharger(self):
		"""
		Method for driving off charger
		"""
		self.conn.behavior.drive_off_charger()

	def playAnim(self, animName):
		"""
		Plays then anim of animName
		"""
		if(animName in self.conn.anim.anim_list):
			self.conn.anim.play_animation(animName)
		else:
			self.conn.behavior.say_text("Not a real animation")

	def dockCube(self):
		"""
		docks to cube
		"""
		conn.world.connect_cube()
		if conn.world.connected_light_cube:
			conn.behavior.dock_with_cube(conn.world.connected_light_cube)

	def showViewer(self, duration):
		"""
		Shows the camera feed
		
		NOT FUNCTIONAL
		"""
		self.conn.viewer.show(timeout=10.0)
		time.sleep(duration)
		self.conn.viewer.close()

	def liftMotors(self, speed):
		"""
		Set lift motors to go up (postive) and down (negative)
		"""
		self.conn.motors.set_lift_motor(speed)

	def headMotors(self, speed):
		"""
		Set head motors to go up (postive) and down (negative)
		"""
		self.conn.motors.set_head_motor(speed)

	def streamWavFile(self, file, volume):
		"""
		Streams the wav file passed
		"""
		self.conn.audio.stream_wav_file(file, volume)

	def sayText(self, text):
		"""
		Vector says the text passed
		"""
		self.conn.behavior.say_text(text)