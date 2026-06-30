""" Variables are like containers for data (i.e. they hold the data) and the value of the variable can vary throughout the program.

Declaring a variable:
Syntax: var_name = literal_value

where var_name is the name given to the container holding the value specified as literal_value in the syntax above.

Example: weight=10

In the above example, weight is the container holding the value 10  which can change during the execution of the program.

 

Python may have data belonging to different types. Common data types used in programming are listed below: 

Category

Datatype

Example

Numeric

int

123

long

1237126381763817

Numeric with decimal point

float

123.45

double

123123.32345324

Alphanumeric

char

A

string

Hello

Boolean

boolean

True, False

 
Python is a dynamically typed language!
In the above example, no datatype was mentioned at the time of declaring variable. In Python, the datatype of a variable is decided automatically at the time of execution based on the value assigned to it. This is called as dynamic typing.

num=65 #line 1

num="A" #line 2

In line 1, variable num is assigned a value 65 which is an integer, so the data type of num variable is integer in line 1.

In line 2, variable num is assigned a value “A” which is a string, so the data type of the num variable is string in line 1.

Note: To check the datatype of the variable we can use type(var_name) which in turn returns the datatype of the variable.

"""


num=66
print(num,type(num))
num="A"
print(num,type(num))
