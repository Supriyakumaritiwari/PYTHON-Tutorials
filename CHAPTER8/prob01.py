

def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
x= 100
y=20
z=30
print("Greatest", greatest(x,y,z))