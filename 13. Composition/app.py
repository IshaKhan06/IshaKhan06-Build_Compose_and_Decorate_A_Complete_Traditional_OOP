'''Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.'''

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  
    def start(self):
        print(f"The {self.brand} car is starting.")
        self.engine.start() 


engine = Engine()
car = Car("BMW", engine)
car.start() 
