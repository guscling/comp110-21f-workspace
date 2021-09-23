points: int = 0
opp_ponits: int = 0
player = None

def main():
    def greet(name) -> None: 
        name = None
        global player
        player = input("What is your name? ")
        print("Hello, " + player + ", how are you? In this program you will play the card game blackjack. The suits will be signified with the symbols and the value of the card with the number or word")
    greet(player)
    understood = False
    while not understood:
        menu = input("What would you like to do next? [1] Begin the game. [2] Quit and see your points.")
        if menu == "1":
            print("Great! lets play")
                
            understood = True
        elif menu == "2":
            print("Thanks for playing! You finished with " + str(points) + " hands won")
            understood = True
            
        else:
            print("I don't understond")

    print("good")



if __name__ == "__main__":
    main()
