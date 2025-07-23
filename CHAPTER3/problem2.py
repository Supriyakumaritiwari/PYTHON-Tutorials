#write a program to detect double spaces in a string ...............


sentence = "harry is a good  boy  bestest"
x = sentence.find("  ")
print(x)


#replace double spaces with single spaces---------------------


print(sentence.replace("  "," "))