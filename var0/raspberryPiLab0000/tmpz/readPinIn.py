import RPi.GPIO as GPIO
import time

pinIn = 16
sleepTime = 0.3333

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinIn,GPIO.IN)
while True:
  pinInValue = GPIO.input(pinIn)
  print( "pinInValue=" + str(pinInValue) )
  time.sleep(sleepTime)

