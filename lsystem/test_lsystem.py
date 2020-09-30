import unittest

from lsystem.lsystem import LSystem


class TestSierpinskiArrowhead(unittest.TestCase):
    def setUp(self):
        self.system = LSystem(rules={"A": "B-A-B", "B": "A+B+A"}, start="A")

    def test_init(self):
        self.assertEqual(self.system.iteration, 0)
        self.assertEqual(self.system.state, ["A"])

    def test_iterate_once(self):
        self.assertEqual(self.system.iteration, 0)
        self.system.iterate()
        self.assertEqual(self.system.iteration, 1)
        self.assertEqual(self.system.state, ["B", "-", "A", "-", "B"])

    def test_iterate_three(self):
        self.assertEqual(self.system.iteration, 0)
        self.system.iterate_many(3)
        self.assertEqual(self.system.iteration, 3)
        self.assertEqual("".join(self.system.state), "B-A-B+A+B+A+B-A-B-A+B+A-B-A-B-A+B+A-B-A-B+A+B+A+B-A-B")


class TestAlgae(unittest.TestCase):
    def setUp(self):
        self.system = LSystem(rules={"A": "AB", "B": "A"}, start="A")
        self.expected = [
            "A",
            "AB",
            "ABA",
            "ABAAB",
            "ABAABABA",
            "ABAABABAABAAB",
            "ABAABABAABAABABAABABA",
            "ABAABABAABAABABAABABAABAABABAABAAB"
        ]

    def test_many(self):
        for idx, result in enumerate(self.expected):
            self.assertEqual("".join(self.system.state), result)
            self.assertEqual(self.system.iteration, idx)
            self.system.iterate()


def test_koch_curve():
    # this is an l-system of only one variable
    system = LSystem(rules={"F": "F+F−F−F+F"}, start="F")
    system.iterate_many(2)
    assert system.iteration == 2
    assert "".join(system.state) == "F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F"
