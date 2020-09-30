import unittest

from lsys import LSystem


class TestSierpinski(unittest.TestCase):
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
        self.expected = {
            0: "A",
            1: "AB",
            2: "ABA",
            3: "ABAAB",
            4: "ABAABABA",
            5: "ABAABABAABAAB",
            6: "ABAABABAABAABABAABABA",
            7: "ABAABABAABAABABAABABAABAABABAABAAB"
        }

    def test_many(self):
        for it, result in self.expected.items():
            self.assertEqual("".join(self.system.state), result)
            self.assertEqual(self.system.iteration, it)
            self.system.iterate()
