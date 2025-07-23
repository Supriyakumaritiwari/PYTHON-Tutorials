#A spam comment is defined as a text containing following keywords:
#  "Make a lot of money" , "buy now" , "click this" , "subscribe this"

p1 = "subscribe this"
p2 = "click this"
p3 = "buy now"
p4 = "Make a lot of money"

message = input("enter you comment")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("This comment is a spam ")

else:
    print("not spam")

