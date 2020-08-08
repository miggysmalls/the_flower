import pytest
from libraries.ServoController import PCA9685


@pytest.ficture(scope='module')
def servo_controller_one(address='0x40', debug=False):
    controller_one = PCA9685(address, debug=debug)
    controller_one.setPWMFreq(50)
    return controller_one
