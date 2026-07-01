"""An if statement within another if statement is known as nested if statement. Similarly, any decision logic can be written within an else statement too"""
num1=10
num2=20
num3=30
if(num1>num2):
    if(num1>num3):
        print("num1 is greater")
    else:
        print("num3 is greater")
elif(num2>num3):
    print("num2 is greater")
else:
    print("num3 is greater")
