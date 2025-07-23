class Employee:
  company = "ITC2"
  def show(self):
        print("Employee class methods ")

class Programmer(Employee):
    company = "ITC Google"
    def showlanguages(self):
        print(f"The name is {self.name} and he is good with {self.language}")


a = Employee()
b = Programmer()
print(a.company,b.company) 