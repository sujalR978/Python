"""The flow inside looping statements are controlled using the looping control statements like pass, break and continue.

When we want to stop a loop or break out of it, we can use the break statement.

When we want to skip the remaining statements in the current loop and continue with the next iteration, we can use continue statement.

Example:

Go through the below code, Assume A – Adult passenger, C- Child, FC – Flight Captain, FA – Flight Attendant, SP – Suspicious passenger. 
Also, assume the following conditions:

Flight captains and attendants do not require to check-in

In case suspicious passengers are found, need to declare an emergency at the airport

For other passengers such as adults and children, need to proceed with normal security check"""


for passenger in "A","A", "FC", "C", "FA", "SP", "A", "A":
    if(passenger=="FC" or passenger=="FA"):
        print("No check required")
        continue
    if(passenger=="SP"):
        print("Declare emergency in the airport")
        break
    if(passenger=="A" or passenger=="C"):
        print("Proceed with normal security check")
    print("Check the person")
    print("Check for cabin baggage")


