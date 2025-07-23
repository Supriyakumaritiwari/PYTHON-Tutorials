# wap to check wheather the givne number is prime or not------------------------------------------------------

n = int(input("enter number for checking prime="))

for i in range(2,n):
    if(n%i==0):
        print("number is not prime")
        break
else:
        print("prime")



# WAP to print sum of n natural number----------------------------------------------------


n = int(input("enter number =  "))
i = 0
sum =  0
while(i<=n):
    sum += i
    i +=1 

print(f"{sum} = sum")



# Wap to calculate factorial of a given number--------------------------------------------
n = int(input("enter number =  "))
fact =1
for i in range(1,n+1):
    fact = fact*i

print(f"fact = {fact}")
