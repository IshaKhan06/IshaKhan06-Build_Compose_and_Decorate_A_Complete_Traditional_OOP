'''Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.'''

class Car:
    def __init__(self, brand):
        self.brand = brand  

    def start(self): 
        print(f"The {self.brand} car has started.")

car1 = Car("BMW")
print(car1.brand) 
car1.start()        
