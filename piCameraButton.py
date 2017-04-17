from picamera import PiCamera
import picamera
from time import sleep
from gpiozero import Button
import datetime as dt

camera=PiCamera()
button=Button(17)
frame=1

camera.annotate_background=picamera.Color("Black")
camera.annotate_foreground=picamera.Color("Yellow")

camera.start_preview()

while True:
	try:
		button.wait_for_press()
		timestamp=dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S')


		camera.annotate_text = "Capturing frame " + str(frame) 
		camera.capture('image%03d.jpg' % frame)
		camera.annotate_text = "Captured frame " + str(frame) + " (" + timestamp + ")"
		frame=frame+1
	except KeyboardInterrupt:
		camera.stop_preview()
		break




