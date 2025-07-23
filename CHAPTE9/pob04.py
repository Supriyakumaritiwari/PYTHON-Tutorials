#replace donkey word by   ##### in same file

word = "donkey"

with open("shekhu.txt","r") as f:
    content = f.read()

new = content.replace("Donkey" , "######")

with open("shekhu.txt","w") as f:
    f.write(new)