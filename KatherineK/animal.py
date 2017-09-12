
# Create parent class Animal, with methods run, walk, and display_health
class Animal(object) :
    def __init__(self, name, health=150):
        self.health = health
        self.name = name
        print self.name + " created"

    def walk(self, repeat):
        self.health -= 1 * repeat
        return self

    def run(self, repeat):
        self.health -= 5 * repeat
        return self

    def display_health(self):
        print self.health
        return self

#Creating three instances of Animal class
GwendolyntheGiraffe = Animal("Gwen")
LarrytheLion = Animal("Larry")
BobtheBear = Animal("Bob")

#Walking and Running an instance of Animal class

BobtheBear.walk(3).run(2).display_health()

# create class Dog, inheriting traits from Animal, with method .pet()
class Dog(Animal) :
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)

    def pet(self, repeat):
        self.health += 5 * repeat
        return self

# Create instance of Dog, call methods .run(), .walk(), and .pet()

Rowdy = Dog("Rowdy", 150)
Rowdy.walk(3).run(2).pet(1).display_health()


# Create class Dragon, inheriting from Animal, with method .fly()
class Dragon(Animal) :
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10

    def display(self):
        self.display_health()
        print "I am a dragon"

# Create instance of Dragon, call method .fly()
Puff = Dragon("Puff", 170)
Puff.display()
