class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Lily(Cat):
    def sing(self, sounds):
        return f'{sounds}'

c1 = Simon('simon', 1)
c2 = Sally('sally', 2)
c3 = Lily('lily', 3)

my_cats = [c1, c2, c3]

my_pets = Pets(my_cats)

my_pets.walk()