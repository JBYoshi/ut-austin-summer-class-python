import RPi.GPIO as GPIO
import time

pir_sensor = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0
count_events = 0

try:
    while True:
        time.sleep(0.2)
        new_state = GPIO.input(pir_sensor)
        if new_state == current_state:
            continue
        current_state = new_state
        if current_state == 1:
            count_events += 1
            print("Motion detected: %s" % (count_events))
        else:
            print("Motion no longer detected")
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
