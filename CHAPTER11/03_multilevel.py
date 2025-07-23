class Employeee:
    def __init__(self):
        print("Constructor of Employeee")
    a=0

class Programmer(Employeee):
    def __init__(self):
        print("Constructor of Programmer")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c=3

# o =Employeee()
# print(o.a)


k = Manager()
print(k.a,k.b,k.c)