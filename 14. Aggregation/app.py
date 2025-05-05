'''Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.'''

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: Department has a reference to an Employee

    def display(self):
        print(f"Department: {self.department_name}")
        print(f"Employee: {self.employee.name}, Position: {self.employee.position}")

emp = Employee("Isha", "Manager")
dept = Department("IT", emp)
dept.display()
