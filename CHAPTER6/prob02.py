#total of 40% or atleast 33% for pass each subject  asssume 3 sub input from user

marks1 = int(input("Enter marks 1= "))
marks2 = int(input("Enter marks 2= "))
marks3 = int(input("Enter marks 3= "))

# check for total percentage

total_percentage = (100*(marks1 + marks2 + marks3))/300

if (total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3 >= 33):
    print("you passes this year", total_percentage)

else: 
    print("you failed , try again next year",total_percentage)