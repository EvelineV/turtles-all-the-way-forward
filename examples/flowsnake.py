import os.path
import sys
import time
import turtle
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from lsystem import lsystem  # pylint: disable=wrong-import-position
from ruleturtle import ruleturtle  # pylint: disable=wrong-import-position

if __name__ == "__main__":
    system = lsystem.LSystem(rules={"A": "A-B--B+A++AA+B-", "B": "+A-BB--B-A++A+B"}, start="A")
    system.iterate_many(4)
    moves = system.state
    distance = 10  # px
    angle = 60  # degrees
    screen = turtle.Screen()
    screen.setworldcoordinates(-400, -600, 210, 0)
    t = ruleturtle.RuleTurtle(rules={
        "A": ("forward", distance),
        "B": ("forward", distance),
        "+": ("left", angle),
        "-": ("right", angle)
    })
    t.speed(0)
    #turtle.tracer(0)
    t.draw(moves)
    time.sleep(5)
