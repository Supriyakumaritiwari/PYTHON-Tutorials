def factorial(n):

    if (n==1 or n==0):
        return 1
    return n* factorial(n-1)

n = int(input("Enter nth number:"))
print(f"the factorial of a number is: {factorial(n)}")