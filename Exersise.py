"""Exercise
Write a Python program that displays a message as follows for a given number:

- If it is a multiple of 3, display "Zip"

- If it is a multiple of 5, display "Zap"

- If it is a multiple of both 3 and 5, display "Zoom"

- If it does not satisfy any of the above given conditions, display 'Invalid'"""


# Task - 1

number = int(input("Enter number : "))

if(number % 3 ==0):
    print("zip")


# Task - 2


number1 = int(input("Enter number : "))

if(number1 % 5 ==0):
    print("Zap")

#Task - 3


number2 = int(input("Enter number : "))

if(number2 % 5 ==0 and number2 % 3 ==0):
    print("Zoom")