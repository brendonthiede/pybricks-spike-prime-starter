from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

hub = PrimeHub()
left_wheel = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(left_wheel, right_wheel, 62.4, 128)
attachment = Motor(Port.D, Direction.COUNTERCLOCKWISE)

# Run at 300 deg/s, until it stalls, then relax
attachment.run_until_stalled(speed=300, then=Stop.COAST)
# Now lift the attachment to the desired starting position (90 degrees here)
attachment.run_angle(speed=100, rotation_angle=-90, then=Stop.HOLD)
# Continue with your mission
drive_base.straight(250)
