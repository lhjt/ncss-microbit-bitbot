from microbit import *

class Direction():
    FORWARD = 0
    BACKWARDS = 1

class Speed():
    MAX = 1023
    STOP = 0

class Wheel:
    def __init__(self, wheel_pin, direction_pin) -> None:
        self.wheel_pin = wheel_pin
        self.direction_pin = direction_pin
        self.speed = 0
        self.direction = Direction.FORWARD

        self.direction_pin.write_digital(0)
        self.wheel_pin.write_analog(self.speed)

    def set_speed(self, speed):
        """
        Set the speed of the wheel.
        """
        if self.direction == Direction.FORWARD:
            self.speed = speed
        else:
            self.speed = 1023 - speed

        self.wheel_pin.write_analog(self.speed)

    def set_direction(self, direction):
        """
        Set the direction of the wheel.
        """
        self.direction_pin.write_digital(direction.value)

left_wheel = Wheel(pin0, pin8)
right_wheel = Wheel(pin1, pin12)

left_wheel.set_speed(Speed.MAX)
right_wheel.set_speed(Speed.MAX)


