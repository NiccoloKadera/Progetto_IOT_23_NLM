import RPi.GPIO as GPIO
DO = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(DO, GPIO.IN)
rain_val = GPIO.input(DO)



if rain_val == 1:
    rain_val = 0
else:
    rain_val = 1

print(rain_val)
