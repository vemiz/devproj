''' Captures images by buttonpress.
The images is to be used in a timelapse
'''

import time
from time import gmtime, strftime
import datetime
import picamera
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import cv2

nframes = 18
ncaptured = 0
interval = 300  # Seconds
output = strftime('/media/pi/USB DISK/timelapse/buttontest/img-%d-%m %H:%M.jpg', gmtime())
folder = '/media/pi/USB DISK/timelapse/buttontest2/'
date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")


def button_callback(channel):
    camera.capture(folder + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".jpg")
    print("Captured img:" + folder + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".jpg")


GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(16, GPIO.IN,
           pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(16, GPIO.RISING, callback=button_callback, bouncetime=3000)  # Setup event on pin 10 rising edge

print("Running...")

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    camera.awb_mode = 'incandescent'
    camera.shutter_speed = 8000
    camera.iso = 100
    camera.framerate = 10
    camera.start_preview(resolution=(1440, 1080))
    time.sleep(2)

    while True:
        time.sleep(1)

camera.stop_preview()
GPIO.cleanup()  # Clean up
