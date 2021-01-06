from microbit import *

class Direction():
    FORWARD = 0
    BACKWARDS = 1

class Speed():
    MAX = 1023
    STOP = 0
    RIGHT_MAX = 1020
    TURN_90_AT_MAX = 450
    TURN_180_AT_MAX = TURN_90_AT_MAX * 2 - 50

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
        self.direction = direction
        self.direction_pin.write_digital(direction)

    def stop(self):
        """
        Stops the wheel.
        """
        self.set_speed(Speed.STOP)

class BitBot:
    def __init__(self, left_wheel, right_wheel) -> None:
        self.left_wheel = left_wheel
        self.right_wheel = right_wheel
        
    def drive_forward_max(self):
        """
        Drive the bot forwards at the maximum speed.
        """
        self.left_wheel.set_speed(Speed.MAX)
        self.right_wheel.set_speed(Speed.RIGHT_MAX)

    def drive_at(self, left_speed, right_speed):
        """
        Drive the bot in the current direction at a specific speed.
        """
        self.left_wheel.set_speed(left_speed)
        self.right_wheel.set_speed(right_speed)

    def set_direction(self, direction):
        """
        Set the direction that the bot will travel in.
        """
        self.right_wheel.set_direction(direction)
        self.left_wheel.set_direction(direction)

    def turn_360(self):
        """
        Turn the bot 360 degrees.
        """
        self.right_wheel.stop()
        self.left_wheel.stop()

        self.right_wheel.set_direction(Direction.BACKWARDS)

        self.right_wheel.set_speed(Speed.RIGHT_MAX)
        self.left_wheel.set_speed(Speed.MAX)
        sleep(850)

        self.left_wheel.stop()
        self.right_wheel.stop()

        self.right_wheel.set_direction(Direction.FORWARD)

    def stop(self):
        """
        Stops the bot.
        """
        self.left_wheel.stop()
        self.right_wheel.stop()


sleep(500)

left_wheel = Wheel(pin0, pin8)
right_wheel = Wheel(pin1, pin12)

bot = BitBot(left_wheel, right_wheel)

# # Drive Forward
# bot.drive_forward_max()
# sleep(2000)

# bot.turn_360()
# sleep(50)

# bot.drive_forward_max()
# sleep(2000)
