class Car:
    wheels = 4
    
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print("drive")
        return self

    def stop(self):
        print("stoppped")
        return self


car_1 = Car("Audi","R8","2022","Black")


print(car_1.make)

car_1.drive()
print(car_1.wheels)

Car.wheels = 2
car_1.wheels = 3

print(Car.wheels)
print(car_1.wheels)


car_1.drive().stop()