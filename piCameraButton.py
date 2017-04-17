from picamera import PiCamera
from time import sleep
from gpiozero import Button

camera=PiCamera()
button=Button(17)

frame=1

camera.start_preview()

while True:
	try:
		button.wait_for_press()
		camera.capture('image%03d.jpg' % frame)
		frame=frame+1
	except KeyboardInterrupt:
		camera.stop_preview()
		break




