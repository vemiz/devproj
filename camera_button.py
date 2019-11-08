import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library


def button_callback(channel):
    print("Button was pushed!")


GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(16, GPIO.IN,
           pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(16, GPIO.RISING, callback=button_callback, bouncetime=2000)  # Setup event on pin 10 rising edge

print("Running...")

GPIO.cleanup()  # Clean up

