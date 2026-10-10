from pybricks.tools import multitask, run_task, wait
from robot import Robot

intro = ["E2/8", "F2/8", "R/4", "R/4", "R/4"]
pickup = ["E2/8", "F2/8", "E2/8", "F2/8", "E2/8", "F2/8", "D2/8", "F2/8"]


def run(robot):
    robot.hub.speaker.play_notes(intro * 4, 60)
    robot.hub.speaker.play_notes(pickup *4, 80)


if __name__ == "__main__":
    run(Robot())
