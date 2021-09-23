points = 0
understood = False
while not understood:
    menu = input("What would you like to do next? [1] Begin the game. [2] Quit and see your points.")
    if menu == "1":
        print("Great!")
        understood = True
    elif menu == "2":
        print("Thanks for playing! You finished with " + str(points) + " points")
        understood = True
            
    else:
        print("I don't understond")
