import time


def test_full_range_of_all_servos(servo_controller_one):
    while True:
        full_rotate(servo_controller_one, 0)


def full_rotate(servo_controller_one, servo_channel):
    for i in range(500, 2500, 5):
        servo_controller_one.setServoPulse(servo_channel, i)
        time.sleep(0.000001)
    time.sleep(1)
    for i in range(2500, 500, -5):
        servo_controller_one.setServoPulse(servo_channel, i)
        time.sleep(0.000001)
