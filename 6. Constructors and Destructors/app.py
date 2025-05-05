'''Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).'''

class Tracker:
    def __init__(self):
        print("Tracker object created.")

    def __del__(self):
        print("Tracker object destroyed.")

t = Tracker()

del t  # Manually calling destructor to see the message immediately
