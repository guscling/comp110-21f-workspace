"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730398806"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says... ")
random = int(randint(0, 5))
if random == 0:
    print("You will have a great day!")
else:
    if random == 1:
        print("You will win the lottery!")
    else:
        if random == 2:
            print("You will fail Comp 110!")
        else:
            if random == 3:
                print("You will ace the next Comp 110 quiz!")
            else:
                if random == 4:
                    print("You will fall over and scrape your knee!")
                else:
                    if random == 5:
                        print("Don't walk too close to any Volkwagon Jettas today!")

print("Now, go spread positive vibes!")