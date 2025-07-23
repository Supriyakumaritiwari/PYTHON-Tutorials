# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# l = [ "harry ","rohan", "shubham","an" ]
# print(rem(l,"an"))



#python function to write a multiplication table--------------------------------

def mult(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

mult(5)