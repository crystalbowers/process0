import Jetson.GPIO as GPIO
import time

class LED_Controller:
    # Initialize the class and pick your pins for each LED
    def __init__(self, left_led=7, right_led=21):
        self.left_led = left_led
        self.right_led = right_led
        print("done")

        GPIO.setmode(GPIO.BOARD)
        print("eek")
        GPIO.setup(self.left_led, GPIO.OUT)
        GPIO.setup(self.right_led, GPIO.OUT)
        print("ahh")

    def run_left_side(self):
        GPIO.output(self.left_led, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(self.left_led, GPIO.LOW)

    def run_right_side(self):
        GPIO.output(self.right_led, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(self.right_led, GPIO.LOW)

    def run(self, side="both"):
        self.run_left_side()
        self.run_right_side()

    def clean_up(self):
        # Cleanup GPIO pins
        #self.left_led.stop()
        #self.right_led.stop()
        GPIO.cleanup()