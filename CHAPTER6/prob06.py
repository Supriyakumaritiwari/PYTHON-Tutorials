# #calculate grade 
# 90-100  = ex
# 80-90    a
# 70-80    b
# 60-70     c
# 50-60    d
# <50=f

marks = int(input("enter marks value= "))

if(marks>=90 and marks<100):
    print("Extension with : ",marks)


elif(marks>=80 and marks<90):
    print("A Grade with : ",marks)


elif(marks>=70 and marks<80):
    print("B Grade with : ",marks)

elif(marks>=60 and marks<70):
    print("C Grade with : ",marks)

elif(marks>=50 and marks<60):
    print("D Grade with : ",marks)
    
elif(marks>=50):
    print("FAIL .................... : ",marks)