#wap to find wheather a given username contains less than 10 characyer or not.

username = input("Enter name of user = \n")

if(len(username) <= 10):
    print("valid user name - GO ON.......")

else:
    print("not valid user name")