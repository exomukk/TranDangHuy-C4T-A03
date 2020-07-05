class Duck:
    def __init__(self, weight, age, name):
        self.weight = weight
        self.age = age
        self.name = name
        self.start = 0

    def walk(self):
        self.start += 1


    def run(self):
        self.walk()
        self.walk()
        self.walk()

duck1 = Duck(weight=1, age=2, name='Donald')
duck1.walk()

duck2 = Duck(weight=2, age=3, name='Mickey')

print(duck1)
print(duck2)


class VNDuck(Duck):
    def __init__(self, weight, age, name):
        Duck.__init__(self, weight=weight, age=age, name=name)
        self.length = 5

    def walk(self):
        self.start += 2

vn_duck = VNDuck(weight=3, age=2, name="vnDuck")
print(vn_duck.start)
vn_duck.walk()


