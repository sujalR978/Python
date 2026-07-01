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
