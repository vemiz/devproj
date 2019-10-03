from PIL import Image

import numpy as np
import cv2
import picamera
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (1440, 1080)
    camera.awb_mode = 'incandescent'
    camera.shutter_speed = 8000
    camera.iso = 100
    camera.framerate = 10

    camera.start_preview(resolution=(1440, 1080))

    while True:
        sleep(1)

