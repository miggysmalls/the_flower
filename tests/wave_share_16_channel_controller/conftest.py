import pytest
from libraries.ServoController import PCA9685


@pytest.fixture(scope='module')
def servo_controller_one():
    controller_one = PCA9685()
    controller_one.setPWMFreq(50)
    return controller_one
