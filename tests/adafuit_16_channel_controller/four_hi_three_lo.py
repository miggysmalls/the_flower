import time


def test_serial_scan_rotate(servo_kit):
	for i in range(len(servo_kit.servo)):
		servo_kit.servo[i].angle = 180
		time.sleep(1)
		servo_kit.servo[i].angle = 0
		time.sleep(1)


def test_syncro_all_rotate(servo_kit):
	for i in range(len(servo_kit.servo)):
		servo_kit.servo[i].angle = 180
		time.sleep(1)
	for i in range(len(servo_kit.servo)):
		servo_kit.servo[i].angle = 0
		time.sleep(1)
