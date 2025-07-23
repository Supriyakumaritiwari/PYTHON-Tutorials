class Employee:
    language = "python"     #this is clas  attribute
    salary = 1200000

    def __init__(self,name, language , salary):
        self.name =name
        self.salary =  salary                 
        self.language = language                 
        print("I am creating a object")

    def getinfo(self):
        print(f"The Language is {self.language}. The Salary is{self.salary}")
    @staticmethod
    def greet():
        print("Good morning")


Rohan = Employee("Rohan Basu","Java",1500000)
# Rohan.name = "Rohan Robinhood Smith"      #this is object/instance attribute
print(Rohan.name,Rohan.language,Rohan.salary)


