# software engineerin object using list
# position , name, age, level, salary

se1 = ["software engineer","Max","20","junior",5000]
se2 = ["software engineer","Lisa","24","senior",8000]

# list is not perfect data structure for such complex object

# Classes are used for more complex data structures
# Class is a blueprint of object

# class

class SoftwareEngineer:
    #class atrribute, they can be used in instances as well
    alais  = "keyboard magician"

    #special method to initialize the object
    def __init__(self, name, age, level, salary):
        # instance attibutes
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
        

# instance of class
se = SoftwareEngineer("max",20,"junior",5000)
#accessing instances
print(se.name, se.age, se.level, se.salary)
#accessing class attributes
print(se.alais)
print(SoftwareEngineer.alais)

# recap
# create a class(blueprint)
# create a instance(object)
# class vs instance
# instance attribute : defined in __init__(self)
# class attribute
