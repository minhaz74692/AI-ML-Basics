class Vehicle:
    def __init__(self, name = "", wheels = 0):
        self.name = name
        self.wheels = wheels

    def general_usage(self):
        print('Generale Usage: transportation')

    def description(self):
        print("I am a", self.name, "and number of wheels are" , self.wheels)

class Car(Vehicle):
    def __init__(self):
        super().__init__("Car", 4)

    def specific_usage(self ):
        print("Specific usage: carry more then 2 person for a trip")


class Bike(Vehicle):
    def __init__(self):
        super().__init__("Bike", 2)

    def specific_usage(self ):
        print("Specific usage: can carry max 2 person")


if __name__ == "__main__":
    car = Car()
    car.description()
    car.general_usage()
    car.specific_usage()

    bike = Bike()
    bike.description()
    bike.general_usage()
    bike.specific_usage()

    #     check
    print("Is instance: ", isinstance(car, Bike))
    print("Is subclass: ", issubclass(Car, Vehicle))
    print("Is subclass: ", issubclass(Car, Bike))

