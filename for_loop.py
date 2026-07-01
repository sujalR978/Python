"""for loop:
In Python, the for loop allows the loop to run over a specific sequence of values. In other words, for every value in the sequence, the loop runs once. Thus, we can avoid infinite loops by using a for loop."""

# https://infyspringboard.onwingspan.com/common-content-store/Shared/Shared/Public/lex_auth_012656924899647488303_shared/web-hosted/assets/for.png


for number in 1,2,3,4,5:
    print("The current number is ",number)

""" Another variation!
In Python, there is an easy way to achieve this by using range(x, y, step). It creates a sequence from x to y-1 with a difference of step between each value. """

start=1
end=10
step=2
for number in range (start, end, step):
    print("The current number is ", number)
