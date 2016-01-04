import RPi.GPIO as GPIO
import time

pinIn = 16
pinOut = 12
sleepTime = 0.2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinIn,GPIO.IN)
GPIO.setup(pinOut,GPIO.OUT)

while True:
  pinInValue = GPIO.input(pinIn)
  print( "pinInValue=" + str(pinInValue) )
      
  if pinInValue:
    GPIO.output(pinOut, True)
    time.sleep(sleepTime)
    GPIO.output(pinOut, False)
  else:
    GPIO.output(pinOut, True)
                          
  time.sleep(sleepTime)

