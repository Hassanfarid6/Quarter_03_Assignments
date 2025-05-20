# 14. Aggregation Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department 
# object store a reference to an Employee object that exists independently of it.

class Employee:

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def details(self):
        print(f"Employee: {self.name}, Job: {self.job}")
        



class Department:

    def __init__(self, dept, employee):
        self.dept = dept
        self.employee = employee
        

    def show (self):
        print(f"Department Name: {self.dept}")
        print(f"Employee in Department ")
        self.employee.details()



emp = Employee("Ali", "Teacher")
    
dept = Department("Math Department", emp)

dept.show()


emp.details()