import RPi.GPIO as GPIO
from time import sleep


class MOTOR():
    pwmr = None

    def __init__(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        self.pwmr = GPIO.PWM(7, 100)
        self.pwmr.start(0)
        self.pwml = GPIO.PWM(15, 100)
        self.pwml.start(0)

    def rfwd(self):
        GPIO.output(3, True)
        GPIO.output(5, False)

    def lfwd(self):
        GPIO.output(11, True)
        GPIO.output(13, False)

    def lrwd(self):
        GPIO.output(11, False)
        GPIO.output(13, True)

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

    def ldr(self, spd=50):
        if spd < 0:
            self.lrwd()
            self.pwml.ChangeDutyCycle(-1 * spd)
        else:
            self.lfwd()
            self.pwml.ChangeDutyCycle(spd)

    def rstop(self):
        GPIO.output(3, False)
        GPIO.output(5, False)
        self.pwmr.ChangeDutyCycle(0)

    def lstop(self):
        GPIO.output(11, False)
        GPIO.output(13, False)
        self.pwml.ChangeDutyCycle(0)

    def dr(self, spd =50):
        self.rdr(spd)
        self.ldr(spd)

    def stop(self):
        self.rstop()
        self.lstop()

m = MOTOR()

m.dr(50)
sleep(2)
m.dr(-50)
sleep(2)
m.stop()
