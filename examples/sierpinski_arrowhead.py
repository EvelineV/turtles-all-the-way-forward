import os.path
import sys
import time
import turtle
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from PIL import Image

from lsystem import lsystem  # pylint: disable=wrong-import-position
from ruleturtle import ruleturtle  # pylint: disable=wrong-import-position

if __name__ == "__main__":
    system = lsystem.LSystem(rules={"A": "B-A-B", "B": "A+B+A"}, start="A")
    system.iterate_many(4)
    moves = system.state
    distance = 10  # px
    angle = 60  # degrees
    screen = turtle.Screen()
    screen.setworldcoordinates(0, 0, 160, 160)
    t = ruleturtle.RuleTurtle(rules={
        "A": ('forward', distance),
        "B": ('forward', distance),
        "+": ('left', angle),
        "-": ('right', angle)
    })
    t.draw(moves)
    name = "sierpinski"
    screen.getcanvas().postscript(file="{}.eps".format(name))
    pic = Image.open("{}.eps".format(name))
    pic.load()
    pic.save("{}.png".format(name))
    time.sleep(10)
