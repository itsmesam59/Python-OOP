# inherits, extends, overrides

class Employee:                      # super / parent class

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):                  # super class function, works in all classes
        print(f"{self.name} is working......")

# inheritance
class SoftwareEngineer(Employee):     # sub / child class

    # extends
    def __init__(self, name, age, salary, project):
        super().__init__(name, age, salary)
        self.project = project

    def debug(self):                 #sub class function, works only in this class
        print(f"{self.name} is debugging")

    # overrides , same fuc=nc name but diff fucntionality
    def work(self):
        print(f"{self.name} is coding")

# inheritance
class Designer(Employee):             # sub / child class

    # extends
    def __init__(self, name, age, salary, design):
        super().__init__(name, age, salary)
        self.design = design

    def draw(self):            # sub class function, works only in this class
        print(f"{self.name} is drawing")

    # overrides, same fuc=nc name but diff fucntionality
    def work(self):
        print(f"{self.name} is designing")

se = SoftwareEngineer("Max", 22, 5000, "Website")
se.work()
se.debug()

de = Designer("phillip", 27, 7000, "front-design")
de.work()
de.draw()

# polymorphism (many shapes)

employees = [SoftwareEngineer("Max", 22, 5000, "Website"),
             Designer("phillip", 27, 7000, "front-design")]

def motivate(employees):
    for x in employees:
        x.work()  # this will work on all class but specific implementation of child class (diff shapes)
        # In polymorphism, we can execute the same method for all classes (work())

motivate(employees)

# Recap :
# inheritance: ChildClass(BaseClass)
# inherit, extend, overrride
# super().__init__()
#polymorphism
