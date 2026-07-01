"""Write a Python program to find the sum of digits of a given number.

Example: Sum of digits of the number 123 will be 6

Note: Initialize the number with various values and test your program."""

num = input("Enter digit : ")

sum = 0;
for number in num:
    sum+=int(number);
print(sum);    

