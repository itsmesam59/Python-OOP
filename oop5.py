
class Employee:
    def __init__(self):
        self.salary = None

    @property                      # get salary , same name as attribute(salary)
    def salary(self):
        return self._salary

    @salary.setter                 # set salary , same name as attribute(salary)
    def salary(self, value):
        self._salary = value

    @salary.deleter                # delete salary, same name as attribute(salary)
    def salary(self):
        del self._salary

    
        

e = Employee()

e.salary = 6000

print(e.salary)
#del e.salary
print(e.salary)

# Recap :
# getter -> @property
# setter -> @x.setter
