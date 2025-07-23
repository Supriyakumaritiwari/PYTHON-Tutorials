'''print multiplication table-----------------------------------
for loop uses'''

num =  int(input("enter a number"))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")





'''print multiplication table-----------------------------------
while loop uses'''



num =  int(input("enter a number"))

i = 0
while(i<=10):
    print(i*num)
    i+=1


    '''Wap to greet all the persons name stored inlist whose name starts with s ----------------------------------'''

l = ["Harry", "Soham", "SAchin","Rahul","kiran","Shekhar"]

for i in l:
    if i.startswith("S"):
        print(f"Hello {i}")
