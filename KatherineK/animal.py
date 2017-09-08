
# Create parent class Animal, with methods run, walk, and display_health
class Animal(object) :
    def __init__(self, name, health=150):
        self.health = health
        self.name = name
        print self.name + " created"

    def walk(self):
        self.health -= 1

    def run(self):
        self.health -= 5

    def display_health(self):
        print self.health

#Creating three instances of Animal class
GwendolyntheGiraffe = Animal("Gwen")
LarrytheLion = Animal("Larry")
BobtheBear = Animal("Bob")

#Walking and Running an instance of Animal class
for i in range (0, 3):
    BobtheBear.walk()
for i in range (0, 2):
    BobtheBear.run()
BobtheBear.display_health()

# create class Dog, inheriting traits from Animal, with method .pet()
class Dog(Animal) :
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health += 5

# Create instance of Dog, call methods .run(), .walk(), and .pet()

Rowdy = Dog("Rowdy", 150)
for i in range (0, 3):
    Rowdy.walk()
for i in range (0, 2):
    Rowdy.run()
Rowdy.pet()
Rowdy.display_health()


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
