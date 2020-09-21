from time import sleep
from gpiozero import LED
from gpiozero import AngularServo
from gpiozero import DistanceSensor


sensor = DistanceSensor(23, 24)
green = LED(5)
yellow = LED(6)
red = LED(26)
servo = AngularServo(17, min_angle=-90, max_angle=90)


while True:
    print(f"Distance to nearest object is {sensor.distance * 100} cm.")
    if sensor.distance >= 1:
        servo.min()
        green.on()
        yellow.off()
        red.off()
    elif sensor.distance >= .5 and sensor.distance < 1:
        servo.mid()
        yellow.on()
        green.off()
        red.off()
    else:
        servo.max()
        red.on()
        yellow.off()
        green.off()
    sleep(1)

