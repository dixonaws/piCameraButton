from picamera import PiCamera
from time import sleep
from gpiozero import Button

camera=PiCamera()
button=Button(17)

camera.start_preview()
button.wait_for_press()
camera.capture('image.jpg')
camera.stop_preview()


