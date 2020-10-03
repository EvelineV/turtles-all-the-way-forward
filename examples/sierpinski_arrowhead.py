import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from lsystem import lsystem  # pylint: disable=wrong-import-position
from ruleturtle import ruleturtle  # pylint: disable=wrong-import-position

if __name__ == "__main__":
    system = lsystem.LSystem(rules={"A": "B-A-B", "B": "A+B+A"}, start="A")
    system.iterate_many(4)
    moves = system.state
    t = ruleturtle.RuleTurtle(rules={
        "A": ('forward', 20),  # px
        "B": ('forward', 20),
        "+": ('left', 60),  # degrees
        "-": ('right', 60)
    })
    t.draw(moves)
