import turtle
from typing import Any, Dict, Iterable


class RuleTurtle(turtle.Turtle):
    def __init__(self, rules: Dict[str, Any], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rules = rules

    def draw(self, moves: Iterable[str]):
        for m in moves:
            action = self.rules.get(m)
            if not action:
                continue
            fname, param = action
            getattr(self, fname)(param)
