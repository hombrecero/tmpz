import RPi.GPIO as GPIO
import time

pinOut = 12
sleepTime = 2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinOut,GPIO.OUT)
while True:
  GPIO.output(pinOut, True)
  time.sleep(sleepTime)
  GPIO.output(pinOut, False)
  time.sleep(sleepTime)

  