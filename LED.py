import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

for i in range(1, 8):
 print 'LED on'
 GPIO.output(18,GPIO.HIGH)
 time.sleep(random.randint(1, 7))
 print 'LED off'
 GPIO.output(18,GPIO.LOW)
 time.sleep(1.5)
