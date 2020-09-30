from typing import Dict, List


class LSystem:
    def __init__(self, rules: Dict[str, str], start: str) -> None:
        self.iteration = 0
        self.state = [start]
        self.rules = rules

    def apply_rule(self, x: str) -> str:
        return self.rules.get(x, x)

    def iterate(self) -> None:
        new_state = []  # type: List
        for x in self.state:
            new_state += self.apply_rule(x)
        self.state = new_state
        self.iteration += 1

    def __str__(self) -> str:
        return "{}: {}".format(self.iteration, " ".join(self.state))

    def iterate_many(self, num: int) -> None:
        for i in range(num):
            self.iterate()
