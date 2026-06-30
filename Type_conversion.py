"""When we perform any operation on variables of different datatypes, the data of one variable will be converted to 
a higher datatype among the two variables and the operation is completed. This conversion is done by interpreter 
automatically and it is known as implicit type conversion. But Python does not support implicit type conversion and 
it will throw an error."""

num1 = 10
num2 = "20" 
# result = num1+ num2. this code give error.
# print("result=%2d" %result)



"""If we have to avoid this, then we have to explicitly convert the datatype of one variable into the required datatype to complete the operation. This is known as explicit type conversion."""

num1= 20
num2 = "40"
result = num1+ int(num2)
print(result)

"""Note:

Programming languages define their own rules for implicit and explicit conversions. These rules do change from language to language."""