class Employee:
  company = "ITC2"
  def show(self):
        print("Employee class methods ")

class Coder:
    language ="Python"
    def printlanguage(Self):
        print(f"The language of the code employee is ")

class Programmer(Employee, Coder):
    Company = "ITC Google"
    def showlanguages(self):
        print(f"The name is {self.Company} and he is good with {self.language}")


a = Employee()
b = Programmer()
print(a.company,b.company,b.language) 
b.show()
a.show()
b.showlanguages()