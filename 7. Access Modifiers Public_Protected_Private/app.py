''' reate a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.'''

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public
        self._salary = salary    # Protected (by convention)
        self.__ssn = ssn         # Private

emp = Employee("Isha", 50000, "123-45-6789")

# Accessing public variable
print("Public:", emp.name)

# Accessing protected variable
print("Protected:", emp._salary) 

# Accessing private variable (will cause AttributeError)
try:
    print("Private:", emp.__ssn)
except AttributeError as e:
    print("Private access error:", e)

# Correct way to access private variable (name mangling)
print("Private (via mangling):", emp._Employee__ssn)
