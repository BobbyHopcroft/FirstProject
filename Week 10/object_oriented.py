class Inhabitant:
    MAX_ENERGY = 100
    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY): pass
    pass


class Human(Inhabitant):
    def __init__(self, name):
        super().__init__(name)
    def __repr__(self):
        return f"Human(name='{self.name}')"
    def __str__(self):
        return f"I am a called {self.name}"
    def display(self):
        print(f"Hello I am a  {self.name}")

class Robot(Inhabitant):
    def __init__(self, name):
        super().__init__(name)
    def __repr__(self):
        return f"Robot(name='{self.name}')"
    def __str__(self):
        return f"I am a {self.name}"
    def display(self):
        print(f"Hello I am a {self.name}")
    def the_rules(self):
        pass


if __name__ == "__main__":
    human = Human("James")
    print(repr(human))
    human.move(10)
    max_energy = 100

if __name__ == "__main__":
    robot = Robot("Robert")
    print(repr(robot))
    robot.move(10)
    max_energy = 100
