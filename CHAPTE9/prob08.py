with open("this.txt") as f :
    contnt = f.read()

with open("this_copy.txt" , "w") as f :
    f.write(contnt)