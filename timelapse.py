import time
import picamera

nframes = 120
interval = 300  # Seconds
folder = '/media/usb/timelapses/groot/'

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    camera.awb_mode = 'incandescent'
    camera.shutter_speed = 8000
    camera.iso = 100
    camera.framerate = 10
    camera.start_preview(resolution=(1440, 1080))
    time.sleep(2)

    ncaptured = 0

    for filename in camera.capture_continuous(folder + 'img{counter:04d}.jpg'):
        ncaptured = ncaptured + 1
        if ncaptured == nframes:
            break
        time.sleep(interval)

print('Timelapse finished with number of captures: ' + str(ncaptured))





