# # star pattern ---------------
# #   *       n = 3
# #  ***
# # *****

# n = int(input("enter number =  "))

# for i in range(1, n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end = "")
#     print(" ")



# '''satar pattern 
# *         n = 3
# **
# ***
# ---------------------------'''
# for i in range(1,4):
#     print("*"* i , end="")
#     print("")



# '''Star Pattern questions

# ***
# * *          n = 3
# ***
# -----------------------------------'''

n = int(input("enter number =  "))
for i in range(1, n+1):
    if (i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*",end="")
    print("")

        