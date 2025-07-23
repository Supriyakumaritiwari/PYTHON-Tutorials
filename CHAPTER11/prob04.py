#write a class complextorepresent a complex number, along with methods to add, subtract, and multiply complex numbers.withoverloading of operators. '+',  and '*'

class Comp:
  def __init__(self,r,i):
    """Initialize a complex number with real and imaginary parts."""
    self.r= r
    self.i = i

  def __add__(self, c2):
      return Comp(self.r + c2.r, self.i+ c2.i)
    
  def __str__(self):
        return f"{self.r} + {self.i}i"
c1 = Comp(2,3)
c2 = Comp(4,5)
print(c1 + c2)  