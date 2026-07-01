"""Write a Python program to check whether the given year is leap year or not.

Write a Python program to find and display the maximum of three given numbers.

Write a Python program to check the given number is prime number or not.

Write a Python program to print first n Fibonacci numbers.

An organization has decided to provide salary hike to its employees based on their job level. Employees can be in job levels 3 , 4 or 5. Hike percentage based on job levels are given below:

Job level

Hike Percentage (applicable on current salary)

3

15

4

7

5

5

 

In case of invalid job level, consider hike percentage to be 0.

Given the current salary and job level, write a Python program to find and display the new salary of an employee"""

# Task - 1
year = int(input("Enter year : "))
if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) :
    print ("year is leap year")


 # Task - 2

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a >= b and a >= c:
    print("A is grater : ",a)
elif b >= a and b >= c:
    print("B is grater : ",b)
else:
      print("c is grater : ",c)


# Task - 3

n = int(input("Enter a number : "))

if n <= 1:
     print("number is not prime ")
else:
    for i in range(2,n):
        if(n % i == 0):
            print("number is not prime : ",n)
            break
        else:
            print("number is prime : ",n)
            break
             

# Task - 4

x = int(input("Enter a number : "))

a = 0
b = 1

if x <= 0 :
    print ("Enter possitive number. ")
elif x == 1 :
    print(x)
else:
    for i in range(x):
        print(a, end = ' ')
        a,b = b,a + b

# Task - 5
# Input current salary and job level
salary = float(input("Enter current salary: "))
job_level = int(input("Enter job level: "))

# Determine hike percentage
if job_level == 3:
    hike = 15
elif job_level == 4:
    hike = 7
elif job_level == 5:
    hike = 5
else:
    hike = 0

# Calculate new salary
new_salary = salary + (salary * hike / 100)

# Display the new salary
print("New Salary =", new_salary)