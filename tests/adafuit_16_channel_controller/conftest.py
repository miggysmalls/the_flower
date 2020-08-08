import pytest
from adafruit_servokit import ServoKit


@pytest.fixture(scope='module')
def servo_kit():
    return ServoKit(channels=16)
