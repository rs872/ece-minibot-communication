


import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

try:
  while True:
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(26,GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
	
except KeyboardInterrupt:
  GPIO.output(19,GPIO.LOW)
  GPIO.output(13,GPIO.LOW)
  print ('interrupt')
  GPIO.cleanup()
  sys.exit(0)





