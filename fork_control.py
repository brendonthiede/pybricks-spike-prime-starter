"""Simple controller for a forklift attachment, connected to ATTACHMENT_1_PORT.

The robot's hardware (hub, wheels, drive base) comes from robot.py,
so if your robot's build changes you only fix it there.
"""

from pybricks.tools import multitask, run_task, wait

from robot import Robot

def run(robot):
    # Move attachment when holding left or right button.
    robot.drive_base.settings(straight_speed=1000, straight_acceleration=2000)

if __name__ == "__main__":
    run(Robot())
