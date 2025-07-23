class Employee:
    language = "python"     #this is clas  attribute
    salary = 1200000

    def getinfo(self):
        print(f"The Language is {self.language}. The Salary is{self.salary}")
    @staticmethod
    def greet():
        print("Good morning")


Rohan = Employee()
Rohan.name = "Rohan Robinhood Smith"      #this is object/instance attribute
print(Rohan.name,Rohan.language,Rohan.salary)
Rohan.greet()
Rohan.getinfo()

