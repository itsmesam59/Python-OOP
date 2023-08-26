# position , name, age, level, salary
se1 = ["software engineer","Max","20","junior",5000]
se2 = ["software engineer","Lisa","24","senior",8000]

# class
class SoftwareEngineer:
    #class atrribute
    alais  = "keyboard magician"

    def __init__(self, name, age, level, salary):
        # instance attibutes
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code")

    def code_language(self,lang):
        print(f"{self.name} is {lang} Developer")
    
    def info(self):
        inofmation  = f"name = {self.name}, age={self.age}, level={self.level}, salary={self.salary}"
        return inofmation
    
    # special or dunder methods

    def __str__(self):   # convert object to string
        inofmation  = f"name = {self.name}, age={self.age}, level={self.level}, salary={self.salary}"
        return inofmation
    
    def __eq__(self,other):   # compare the instances and instance attributes
        return self.name == other.name and self.age == other.age
    
    @staticmethod
    # this method is not tied to any specific instance, its for whole class
    def salaty_age(age):
        if age > 23:
            return 7000
        if age < 23:
            return 5000

        

# instance
se1 = SoftwareEngineer("max",20,"junior",5000)
se2 = SoftwareEngineer("lisa",24,"senior",7000)
se3 = SoftwareEngineer("lisa",24,"senior",7000)

se1.code()
se2.code()

se1.code_language("python")
se2.code_language("C++")

print(se1.info())
print(se2.info())

print(se1)      # printing object will invoke special methods (__str__)
print(se2)

print(se2 == se3)        # comparison (__eq__)

print(se1.salaty_age(24))
print(SoftwareEngineer.salaty_age(22))

# Recap
# instance method(self)
# can take arguments and can return values
# special "dunder" methods (__str__and__eq__)
# @staticmethod