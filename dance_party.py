"""Dance party: wiggle and swirl around while the theme song plays.

The robot's hardware (hub, wheels, drive base) comes from robot.py,
so if your robot's build changes you only fix it there.
"""

from pybricks.tools import multitask, run_task, wait

from robot import Robot
from theme_music import play_theme_song


async def dance(drive_base):
    # Scoot forward and back a little, twice.
    for _ in range(2):
        for distance in (10, -10):
            await wait(1000)
            await drive_base.straight(distance)
    await wait(1000)

    # Swirl around in little arcs: each pair is (radius sign, angle sign).
    arc_steps = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    for _ in range(16):
        for radius_sign, angle_sign in arc_steps:
            await drive_base.arc(100 * radius_sign, 35 * angle_sign)


async def party(robot):
    # Play the song and dance at the same time.
    await multitask(
        play_theme_song(robot.hub),
        dance(robot.drive_base),
    )


def run(robot):
    # Dance fast! Fast moves need fast acceleration too.
    robot.drive_base.settings(straight_speed=1000, straight_acceleration=2000)
    run_task(party(robot))


if __name__ == "__main__":
    run(Robot())
