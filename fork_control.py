"""Drive the forklift attachment by hand with the hub's buttons.

Hold the LEFT button to move the attachment up, hold the RIGHT
button to move it down, and let go to stop. Press CENTER to quit.

The attachment motor needs to be configured as ATTACHMENT_1_PORT in robot.py.
"""

from pybricks.parameters import Button
from pybricks.tools import wait

from robot import Robot

# How fast the attachment moves, in degrees per second.
# Make this smaller for finer control, bigger to move faster.
FORK_SPEED = 500

def run(robot):
    fork = robot.attachment_1
    if fork is None:
        print("No attachment motor! Set ATTACHMENT_1_PORT in robot.py first.")
        return

    # Keep checking the buttons until the CENTER (stop) button is pressed.
    while True:
        pressed = robot.hub.buttons.pressed()

        if Button.LEFT in pressed:
            # Hold LEFT: move at a positive speed.
            fork.run(FORK_SPEED)
        elif Button.RIGHT in pressed:
            # Hold RIGHT: move at a negative speed.
            fork.run(-FORK_SPEED)
        else:
            # No button held: stop and hold the fork where it is.
            # `hold` tries to keep its position
            fork.hold()

        # A short pause so the hub isn't checking the buttons nonstop.
        wait(20)


# Lets you run JUST this program: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
