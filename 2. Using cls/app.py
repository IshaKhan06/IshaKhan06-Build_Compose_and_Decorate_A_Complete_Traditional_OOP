'''Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.'''


class Counter:
    count = 0  

    def __init__(self):
        Counter.count += 1  

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.display_count()
