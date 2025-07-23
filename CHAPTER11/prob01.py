# create class 2d vctor that represent 3dvector

class TwoDVector:
    def  __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"the Vector is {self.i}i + {self.j}j ")

class ThreeDVector(TwoDVector):
     def  __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
     def show(self):
        print(f"the Vector is {self.i}i + {self.j}j + {self.k}k ")


m = TwoDVector(1,2)
n= ThreeDVector(3,4,5)
m.show()
n.show()
