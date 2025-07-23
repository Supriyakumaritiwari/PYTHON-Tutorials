#replace donkey word by   ##### in same file

words = ["Donkey", "bad", "ganda"]

with open("shekhu.txt","r") as f:
    content = f.read()


for word in words:
    content = content.replace(word , "#" * len(word))

with open("shekhu.txt","w") as f:
    f.write(content)