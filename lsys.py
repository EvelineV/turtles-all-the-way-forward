class LSystem:
    def __init__(self, rules, start):
        self.iteration = 0
        self.state = [start]
        self.rules = rules

    def apply_rule(self, x):
        return self.rules.get(x, x)

    def iterate(self):
        new_state = []
        for x in self.state:
            new_state += self.apply_rule(x)
        self.state = new_state
        self.iteration += 1
    
    def __str__(self):
        return "{}: {}".format(self.iteration, " ".join(self.state))

    def iterate_many(self, num):
        for i in range(num):
            self.iterate()

