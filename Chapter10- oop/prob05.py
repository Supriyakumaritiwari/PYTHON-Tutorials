#class train
import random
class Train:
    def __init__(self,trainno):
        self.trainno= trainno 

    def book(self,trainno,fro,to):
        print(f"Booking ticket for Train {trainno} from {fro} to {to}")
    
    def getstatus(self,trainno):
        print(f"Status of train {trainno} is running on time")

    def getfare(self,trainno,fro,to):
        print(f"The fare of train{trainno} fromv{fro} to {to} is {random.randict(200,1500)}")

    
t = Train(22857)
t.book(22579,"DTO " ,"STA")
