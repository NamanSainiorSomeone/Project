class Animal:

    alive = True

    def eat(g):
        print("eats")

    def sleep(g):
        print("sleep")


class Rabbit(Animal):
    pass

class Fish(Animal):
    pass

rabbit = Rabbit()
fish = Fish()

print(rabbit.alive)
fish.eat()