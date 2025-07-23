#wap to read the text fom a given file 'poem.txt' and find out wheather it contain the word twinkle

f = open("poem.txt")
content = f.read()

if("twinkle" in content):
    print("twinkle is pesent in the file")
f.close()