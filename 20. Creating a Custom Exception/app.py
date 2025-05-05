'''Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.'''

class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age is less than 18, which is not allowed.")
    else:
        print("Age is valid.")


try:
    check_age(10)  
except InvalidAgeError as e:
    print(f"Error: {e}")
