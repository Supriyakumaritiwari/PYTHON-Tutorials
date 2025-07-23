# check the word "python" is presenr or not in logfile

# with open("log.txt") as f:
#     content = f.read()

# if("python" in content):
#     print("Yes python present in log file")

# else:
#     print("Not present python")



# give output at which line python word is present


with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python present in log file in line no = {lineno} ")
        break
    lineno+= 1
else:
     print("Not present python")