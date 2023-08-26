 # Encapsulation :- hiding the data implementation

class Employee:
    def __init__(self, name, age):
        self.name = name      # public attributes
        self.age = age

        # used internally 
        self._salary = 5000   # _salary is protected attribute(1 _)
        self.__bugsolved = 500 # _bugssolves is private attribute(2 __)

    # internal attribute only be accessed from outside only using getter and setter 

    def code(self):
        self.__bugsolved += 1
    # getter
    def get_salary(self):
        return self._salary

    # setter
    # check value enforce constraint
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self.__bugsolved < 10:
            return base_value
        if self.__bugsolved < 100:
            return base_value * 2
        return base_value * 3
        

e = Employee("sam",20)
print(e.name,e.age)

for i in range(70):
    e.code()

e.set_salary(1000)                # abstarction
print(e.get_salary())

# abstraction :- natural extension of encapsulation
# Each object should only expose high level mechanism for user
# this mechanism should hide internal mechanism

# Recap 
# encapsulation
# abstraction
# public, private methods and attributes
# _func(), _attribute
# getter / setter to access internal attributes from outside