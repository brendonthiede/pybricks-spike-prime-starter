from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait

from theme_music import play_theme_song

hub = PrimeHub()
left_wheel = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(left_wheel, right_wheel, 62.4, 128)
drive_base.settings(straight_speed=1000)
drive_base.settings(straight_acceleration=2000)

async def dance():
    for _ in range(2):
        for distance in (10, -10):
            await wait(1000)
            await drive_base.straight(distance)
    await wait(1000)

    arc_steps = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    for _ in range(16):
        for radius_sign, angle_sign in arc_steps:
            await drive_base.arc(100 * radius_sign, 35 * angle_sign)

async def main():
    await multitask(
        play_theme_song(hub),
        dance(),
    )


run_task(main())