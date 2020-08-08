import pytest
from adafruit_servokit import ServoKit


@pytest.fixture(scope='Module')
def servo_kit():
    return ServoKit(channels=16)
