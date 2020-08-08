import time


def test_full_range_of_all_servos(servo_controller_one):
    max_runs = 3
    while max_runs != 0:
        full_rotate(servo_controller_one, 0)
        full_rotate(servo_controller_one, 1)
        full_rotate(servo_controller_one, 2)
        full_rotate(servo_controller_one, 3)
        full_rotate(servo_controller_one, 4)
        full_rotate(servo_controller_one, 5)
        full_rotate(servo_controller_one, 6)
        max_runs -= 1


def full_rotate(servo_controller_one, servo_channel):
    for i in range(500, 2500, 100):
        servo_controller_one.setServoPulse(servo_channel, i)
        time.sleep(0.01)
    time.sleep(1)
    for i in range(2500, 500, -100):
        servo_controller_one.setServoPulse(servo_channel, i)
        time.sleep(0.01)
