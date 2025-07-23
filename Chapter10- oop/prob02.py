#class calculator finding square cube and squareroot

class Calculator():

    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")
    
    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")
    
    def squareroot(self):
        print(f"The squareroot of {self.n} is {self.n**0.5}")
    
   
    
calci = Calculator(4)
calci.square()
calci.cube()
calci.squareroot()