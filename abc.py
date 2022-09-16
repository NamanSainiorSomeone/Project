from abc import ABC , abstractmethod

class Animal(ABC):
    
    alive = True
    @abstractmethod
    def eat(g):
        print("eats")

    def sleep(g):
        print("sleep")


class Rabbit(Animal):
    def eat(g):
        print("eats")

class Fish(Animal):
    def eat(g):
        print("eats")

rabbit = Rabbit()
fish = Fish()

print(rabbit.alive)
fish.eat()