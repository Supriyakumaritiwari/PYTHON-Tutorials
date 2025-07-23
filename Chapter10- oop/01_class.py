class Employee:
    language = "python"     #this is clas  attribute
    salary = 1200000

obj = Employee()
print(obj.name)

Rohan = Employee()
Rohan.name = "Rohan Robinhood Smith"      #this is object/instance attribute
print(Rohan.name,Rohan.language,Rohan.salary)