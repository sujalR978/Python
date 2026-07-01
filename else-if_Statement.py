"""else-if ladder:
It is a conditional statement used for selection between multiple set of statements based on multiple test conditions. The various test conditions are provided inside each if-elif statement. Whenever the test condition is evaluated as True, the statements inside the corresponding block are executed and the control comes out of the else-if ladder. If none of the test conditions are evaluated as True, the statements inside the else block are executed. As we have multiple set of statements to select based on the test conditions, it is also called as multi-way selection statement.

In else-if ladder, the conditions are evaluated from the top of the ladder downwards. As soon as a True condition is found, the set of statements associated with it get executed skipping the rest of the ladder."""

# https://infyspringboard.onwingspan.com/common-content-store/Shared/Shared/Public/lex_auth_012656924899647488303_shared/web-hosted/assets/elif.png


a=0
if(a>0):
    print("positive integer")
elif(a<0):
    print("negative integer")
else:
    print("it’s zero")
