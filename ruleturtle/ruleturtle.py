import turtle
from typing import Any, Dict, Iterable


class RuleTurtle(turtle.Turtle):
    def __init__(self, rules: Dict[str, Any], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rules = rules
        self.saved_position = self.position()
        self.saved_heading = self.heading()

    def save_position(self, *args, **kwargs):  # pylint:disable=unused-argument
        self.saved_position = self.position()
        self.saved_heading = self.heading()

    def return_to_saved_position(self, *args, **kwargs):  # pylint:disable=unused-argument
        self.penup()
        self.goto(self.saved_position)
        self.setheading(self.saved_heading)
        self.pendown()

    def draw(self, moves: Iterable[str]):
        for m in moves:
            action = self.rules.get(m)
            if not action:
                continue
            fname, param = action
            getattr(self, fname)(param)
