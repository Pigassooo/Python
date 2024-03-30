class Vehicle:
    def general_usage(self):
        print('transportation')

class Car(Vehicle):
    def __init__(self):
        print("I'm a car")

c = Car()

print(isinstance(c, Vehicle))