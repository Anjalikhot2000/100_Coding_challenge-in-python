#1. User will input (3ages).Find the oldest one

per1=int(input("Enter the age of person 1: "))
per2=int(input("Enter the age of person 2: "))
per3=int(input("Enter the age of person 3: "))
age=max(per1,per2,per3)
print("The oldest age is: ",age)