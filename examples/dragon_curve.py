import os.path
import sys
import time
import turtle

from PIL import Image

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from lsystem import lsystem  # pylint: disable=wrong-import-position
from ruleturtle import ruleturtle  # pylint: disable=wrong-import-position

if __name__ == "__main__":
    system = lsystem.LSystem(rules={"X": "X+YF+", "Y": "−FX−Y"}, start="FX")
    system.iterate_many(10)
    moves = system.state
    screen = turtle.Screen()
    screen.setworldcoordinates(-100, -700, 600, 100)
    distance = 20  # px
    angle = 90  # degrees
    t = ruleturtle.RuleTurtle(rules={
        "F": ("forward", distance),
        "-": ("left", angle),
        "+": ("right", angle)
    })
    t.draw(moves)
    name = "dragon-curve"
    screen.getcanvas().postscript(file="{}.eps".format(name))
    pic = Image.open("{}.eps".format(name))
    pic.load()
    pic.save("{}.png".format(name))
    time.sleep(5)
