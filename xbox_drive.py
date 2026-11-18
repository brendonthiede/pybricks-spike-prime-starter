"""Drive the robot around with an Xbox controller.

How to drive:
    LEFT stick  (up / down)     - drive forward and backward
    RIGHT stick (left / right)  - turn left and right
    Y button (hold)             - arm goes UP
    A button (hold)             - arm goes DOWN
    CENTER button on the hub    - quit

Getting the controller connected:
  1. Turn the controller on (press the Xbox button so it lights up).
  2. Hold the small pairing button on the top edge of the controller
     until the Xbox button blinks fast.
  3. Start this program. The hub looks for the controller and the
     program waits until it finds it. The Xbox button stops blinking
     and the hub beeps when you are ready to drive.
  After the first time, you only need steps 1 and 3.

The arm motor needs to be configured as ATTACHMENT_1_PORT in robot.py.
"""

from pybricks.iodevices import XboxController
from pybricks.parameters import Button
from pybricks.tools import wait

from robot import Robot

# How fast the robot drives with the stick pushed all the way,
# in millimeters per second. Make this smaller for a slower, easier
# to control robot.
MAX_DRIVE_SPEED = 400

# How fast the robot turns with the stick pushed all the way,
# in degrees per second.
MAX_TURN_SPEED = 180

# How fast the arm moves, in degrees per second.
# If Y makes the arm go DOWN instead of up, make this number negative.
ARM_SPEED = 500

# Sticks never rest at exactly 0. Any stick number smaller than this
# counts as "not touching the stick", so the robot doesn't creep.
# Stick numbers go from -100 to 100.
STICK_DEAD_ZONE = 10


def stick_to_speed(stick, max_speed):
    """Turn a stick number (-100 to 100) into a speed."""
    if abs(stick) < STICK_DEAD_ZONE:
        return 0
    return stick * max_speed / 100


def run(robot):
    # Keep looking until the controller is connected. The hub only
    # looks for about 10 seconds at a time, so if it doesn't find the
    # controller we just look again.
    controller = None
    while controller is None:
        print("Looking for the Xbox controller...")
        try:
            controller = XboxController()
        except OSError:
            print("Didn't find it. Is the Xbox button blinking FAST?")
            print("Hold the pairing button on top of the controller.")
            wait(500)
    print("Controller connected! Drive away.")
    robot.hub.speaker.beep()

    arm = robot.attachment_1
    if arm is None:
        print("No arm motor! Set ATTACHMENT_1_PORT in robot.py to use the arm.")

    # The gyro tries to keep the robot pointed the same way, which
    # fights you if you pick the robot up or bump it while driving
    # by hand. Turn it off for this program.
    robot.drive_base.use_gyro(False)

    # Keep reading the controller until the CENTER (stop) button
    # on the hub is pressed.
    while True:
        # --- Driving ---
        # Each stick gives two numbers: left/right, then up/down.
        left_stick = controller.joystick_left()
        right_stick = controller.joystick_right()

        drive_speed = stick_to_speed(left_stick[1], MAX_DRIVE_SPEED)
        turn_speed = stick_to_speed(right_stick[0], MAX_TURN_SPEED)

        if drive_speed == 0 and turn_speed == 0:
            # Not touching the sticks: stop the wheels.
            robot.drive_base.stop()
        else:
            robot.drive_base.drive(drive_speed, turn_speed)

        # --- Arm ---
        if arm is not None:
            pressed = controller.buttons.pressed()

            if Button.Y in pressed:
                # Hold Y: arm up.
                arm.run(ARM_SPEED)
            elif Button.A in pressed:
                # Hold A: arm down.
                arm.run(-ARM_SPEED)
            else:
                # No button held: stop and hold the arm where it is,
                # so it doesn't droop under its own weight.
                wait(150)
                arm.hold()

        # A short pause so the hub isn't checking the controller nonstop.
        wait(20)


# Lets you run JUST this program: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
