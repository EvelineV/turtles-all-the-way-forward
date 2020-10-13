import os.path
import sys
import time
import turtle
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from lsystem import lsystem  # pylint: disable=wrong-import-position
from ruleturtle import ruleturtle  # pylint: disable=wrong-import-position

if __name__ == "__main__":
    system = lsystem.LSystem(rules={"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}, start="X")
    system.iterate_many(3)
    moves = system.state
    distance = 5  # px
    angle = 25  # degrees
    screen = turtle.Screen()
    screen.setworldcoordinates(0, -20, 140, 200)
    t = ruleturtle.RuleTurtle(rules={
        "F": ("forward", distance),
        "-": ("left", angle),
        "+": ("right", angle),
        "[": ("save_position", 0),  # save current values for position and angle
        "]": ("return_to_saved_position", 0)  # restore values saved by [
    })
    t.draw(moves)
    time.sleep(5)
