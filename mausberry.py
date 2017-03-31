#!/usr/bin/python3

import RPi.GPIO as GPIO
import signal
import subprocess
import sys
import threading

class Mausberry:
    GPIO_IN = 16
    GPIO_OUT = 18

    def __init__(self):
        self.wait_mutex = threading.Event()
        signal.signal(signal.SIGINT, self.signal_handler)

        GPIO.setmode(GPIO.BOARD)

        # When this pin goes high, the ON/OFF switched is turned off and the
        # machine should shutdown
        GPIO.setup(self.GPIO_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.GPIO_IN, GPIO.RISING, self.shutdown, bouncetime=200)

        # Enable the watchdog, when this pin goes low, the mausberry circuit
        # will cut the power
        GPIO.setup(self.GPIO_OUT, GPIO.OUT)
        GPIO.output(self.GPIO_OUT, 1)

    def run(self):
        try:
            while not self.wait_mutex.wait():
                pass
            return
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()

        sys.exit(0)

    def shutdown(self, gpio_pin):
        subprocess.call(['shutdown', '-P', 'now'])
        pass

    def signal_handler(self, signal, frame):
        self.wait_mutex.set()

if __name__ == '__main__':
    main = Mausberry()
    main.run()
