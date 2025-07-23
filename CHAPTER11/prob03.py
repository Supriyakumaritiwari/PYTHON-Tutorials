#create class 'employee'and add salary and increement properties to it.
#write method'salaryAfterIncrement' with a @property decorator with a setter which changes the value of increment based on the salary

class Employee:

    salary =234
    increment =20

    @property
    def salaryAfterIncrement(self):
        return (self.salary * (1 + self.increment /100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


e = Employee()
print(e.salaryAfterIncrement)  # Output: 280.8
e.salaryAfterIncrement = 280.8
print(e.increment)  # Output: 20.0
        
