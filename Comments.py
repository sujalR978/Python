"""Comments are the lines which are skipped during execution of a program. 

There are two types of comments available in Python:

First one is single line comment which starts with ‘#’ symbol and extends till the end of line. Comments can start from the beginning of the line and middle of the line, but it should not be a part of string literal.

Second one is multi line comment which starts with ''' or "(3) and ends ''' or "(3)  respectively. This type of comment is mainly used for documentation purpose."""

'''
used for: Demonstrating comments 
This is the first way of using multi-line comment
'''
"""
used for: Demonstrating comments 
second way of using multi-line comment
"""
#program to demonstrate explicit type conversion 
num1=10 #variable of integer type
num2="20" #variable of string type
result=num1+int(num2) #using explicit conversion 
print(result)
