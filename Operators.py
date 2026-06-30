"""
Category 

Operators

Arithmetic Operators

+,-,*,/, %,//

Relational Operators

==,!=,>,<,>=,<=

Assignment Operators

=,+=,-=,*=,/=,%=

Logical Operators

and,or,not

 
Arithmetic operators:
Operator

Explanation 

Example

+

Used for addition operation

"+" is used as addition operator where 11+2 is evaluated as 13

-

Used for subtraction operation

"-" is used as subtraction operator where 11-2 is evaluated as 9, 2-11 is evaluated as -9

*

Used for multiplication operation

"*" is used as multiplication operator where 11*2 is evaluated as 22

/

Used for division operation

"/" is used as division operator where 11/2 is evaluated as 5.5

//

Used for integer division operation

"//" is used for integer division where 11//2 is evaluated as 5

%

Used for modulo operation. Consider the expression  num1% num2 which finds the remainder after dividing num1 by num2

"%" is used as modulo operator where 11%2 is evaluated as 1, 9%11 is evaluated as 9

 
Relational operators:
Operator

Explanation

Example

==

Used for checking the equality of two values/variables

10 == 10 is evaluated as True

10 == 100 is evaluated as False

!=

Used for checking the inequality of two values/variables

10 != 10 is evaluated as False

10 != 100 is evaluated as True

>

Used for checking if num1 is greater than num2 and is represented as num1 > num2 

10 > 10 is evaluated as False

100 > 10 is evaluated as True

<

Used for checking if num1 is lesser than num2 and is represented as num1 < num2 

10 < 10 is evaluated as False

10 < 100 is evaluated as True

>=

Used for checking if num1 is greater than or equal to num2 and is represented as num1 >= num2 

10 >= 10 is evaluated as True

10 >= 100 is evaluated as True

<=

Used for checking if num1 is lesser than or equal to num2 and is represented as num1 <= num2 

10 <= 10 is evaluated as True

100 <= 10 is evaluated as False

 
Assignment operators:
Operator

Explanation

Example

=

Used for assigning a value to a variable

num=5

Here num is assigned the value 5 

+=

Used as short hand assignment operator for addition

num=num+1 can also be represented as num+=1

-=

Used as short hand assignment operator for subtraction

num=num-1 can also be represented as num-=1

*=

Used as short hand assignment operator for multiplication

num=num*1 can also be represented as num*=1

/=

Used as short hand assignment operator for division

num=num/1 can also be represented as num/=1

%=

Used as short hand assignment operator for modulo operation

num=num%1 can also be represented as num%=1


Logical Operators:
These operators are used to combine one or more relational expressions.

Operators

Description

AND

Result will be true, if both the expressions are true. If any one or both the expressions are false, the result will be false

OR

Result will be true, even if one of the expression is true. If both the expressions are false, the result will be false

NOT

If the expression is true, result will be false and vice versa

If A and B are two relational expressions, say A = (Num1>2000), B= (Num2>100), the result of combining A and B using logical operator is based on the result of A and B as shown below:

A

B

A and B

True

True

True

True

False

False

False

True

False

False

False

False

 

A

B

A or B

True

True

True

True

False

True

False

True

True

False

False

False

 

A

not A

True

False

False

True

 """
# 1) Arithmetic operators
a = 11
b = 2

print("a + b =", a + b)   # 13
print("a - b =", a - b)   # 9
print("a * b =", a * b)   # 22
print("a / b =", a / b)   # 5.5
print("a // b =", a // b) # 5
print("a % b =", a % b)   # 1


# 2) Relational operators

x = 10
y = 100

print("x == y", x == y)   # False
print("x != y", x != y)   # True
print("x > y", x > y)     # False
print("x < y", x < y)     # True
print("x >= 10", x >= 10) # True
print("y <= 10", y <= 10) # False


# 3) Assignment operators

num = 5
print("num =", num)  # 5

num += 1
print("num += 1 ->", num)  # 6

num -= 1
print("num -= 1 ->", num)  # 5

num *= 2
print("num *= 2 ->", num)  # 10

num /= 2
print("num /= 2 ->", num)  # 5.0

num %= 3
print("num %= 3 ->", num)  # 2.0



# 4) Logical operators

A = 5 > 2      # True
B = 3 > 4      # False

print("A and B =", A and B)   # False
print("A or B =", A or B)     # True
print("not A =", not A)       # False
print("not B =", not B)       # True


# 5) Combined example

num1 = 15
num2 = 4

result = (num1 > num2) and (num1 % num2 == 3)
print(result)  # True




