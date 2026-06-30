"""The print() function:
Python provides the print() built-in function to display the output onto the standard output device (i.e. Monitor)

Syntax: print(“var_name1, var_name2, …”, [end=”value1”, sep=”value2”])

where,

var_name1, var_name2 are the variable names or the literals you want to print or output

end is used to specify the separator between two print statements which is ‘\n’ by default

sep is used to specify the separator between multiple variables displayed using a single print statement"""


a = 'hello'
b = 20.124
c = 90

print(a,b,c)
print(a,b,c,end = " "'\n')
print(a,b,c,sep = ':')
print("b=%0.2f" %b)
print("c=%8d" %c)
print("c=%-8d" %c)


"""
hello 20.124 90
hello 20.124 90 
hello:20.124:90
b=20.12
c=      90
c=90 

"""