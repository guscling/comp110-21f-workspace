"""An exercise in remainders and boolean logic."""

__author__ = "730398806"


# Begin your solution here...
tar: str = "TAR"
heels: str = "HEELS"
carolina: str = "CAROLINA"  
int_input = int(input("Enter an int: "))
if int_input % 2 == 0 and int_input % 7 == 0:
    print(tar + " " + heels)
else:
    if int_input % 2 == 0:
        print(tar)
    else:
        if int_input % 7 == 0:
            print(heels)
        else:
            if int_input % 7 or 2 != 0:
                print(carolina)