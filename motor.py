import RPi.GPIO as GPIO
from time import sleep


class MOTOR():
    pwmr = None

    def __init__(self):
        self.M = 10
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        self.pwmr = GPIO(7, 100)
        self.pwmr.start(0)

    def rfwd(self):
        GPIO.output(3, True)
        GPIO.output(5, False)

    def rrwd(self):
        GPIO.output(3, False)
        GPIO.output(5, True)

    def rdr(self, spd=50):
        if spd < 0:
            self.rrwd()
            self.pwmr.ChangeDutyCycle(-1 * spd)
        else:
            self.rfwd()
            self.pwmr.ChangeDutyCycle(spd)

    def rstop(self):
        GPIO.output(3, False)
        GPIO.output(5, False)
        self.pwmr.ChangeDutyCycle(0)

m = MOTOR()

m.rdr(50)
sleep(2)
m.rdr(-50)
sleep(2)
m.rstop()
