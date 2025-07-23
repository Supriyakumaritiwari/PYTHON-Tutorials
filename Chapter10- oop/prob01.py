
# class for employee working with microsoft

class Programmer:
    company ="Microsoft"

    def __init__(self, name ,salary, pin):
        self.name =name
        self.salary =salary
        self.pin = pin        


p = Programmer("SUPRIYA",3250000, 485001)
print(p.name,p.company, p.salary, p.pin)