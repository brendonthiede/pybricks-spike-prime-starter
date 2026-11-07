"""Drive the forklift attachment by hand with the hub's buttons.

Hold the LEFT button to move the attachment one way, hold the RIGHT
button to move it the other way, and let go to stop. Press CENTER to quit.

Handy for raising or lowering the fork into position before a match, or
for testing how far it can move without writing a whole mission.

The attachment motor is the one plugged into ATTACHMENT_1_PORT in robot.py,
so if your robot's build changes you only fix it there.
"""

from pybricks.parameters import Button
from pybricks.tools import wait

from robot import Robot

# How fast the attachment moves, in degrees per second.
# Make this smaller for finer control, bigger to move faster.
FORK_SPEED = 300

# If LEFT moves the fork the "wrong" way for your robot, change this to -1.
LEFT_DIRECTION = 1


def run(robot):
    fork = robot.attachment_1
    if fork is None:
        print("No attachment motor! Set ATTACHMENT_1_PORT in robot.py first.")
        return

    # Keep checking the buttons until the CENTER (stop) button is pressed.
    while True:
        pressed = robot.hub.buttons.pressed()

        if Button.LEFT in pressed:
            # Hold LEFT: move the fork one way.
            fork.run(FORK_SPEED * LEFT_DIRECTION)
        elif Button.RIGHT in pressed:
            # Hold RIGHT: move the fork the other way.
            fork.run(-FORK_SPEED * LEFT_DIRECTION)
        else:
            # No button held: stop and hold the fork where it is.
            # (Change hold() to stop() if you want the fork to relax instead.)
            fork.hold()

        # A short pause so the hub isn't checking the buttons nonstop.
        wait(20)


# Lets you run JUST this program: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
