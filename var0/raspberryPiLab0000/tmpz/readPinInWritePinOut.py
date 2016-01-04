import RPi.GPIO as GPIO
import time

pinIn = 16
pinOut = 12
sleepTime = 0.3333

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinIn,GPIO.IN)
GPIO.setup(pinOut,GPIO.OUT)

while True:
  pinInValue = GPIO.input(pinIn)
  GPIO.output(pinOut, pinInValue)
  print( "pinInValue=" + str(pinInValue) )
  time.sleep(sleepTime)

