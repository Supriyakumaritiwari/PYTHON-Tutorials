# f = open("file.txt")
# print(f.read())
# f.close()


# The sam can be written "with" stmt through which closing of file not be explicitly needed

with open("file.txt") as f:
    print(f.read())