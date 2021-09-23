import random
points = 0
opp_points: int = 0
player = None
def main():
    THUMBSUP = '\U0001F44D'
    THUMBSDOWN = '\U0001F44E'
    SHRUG = '\U0001F937'
    def greet(name) -> None: 
        name = None
        global player
        player = input("What is your name? ")
        print("Hello, " + player + ", how are you? In this program you will be asked trivia questions by the computer. If you answer correctly you get a point. You will then have a chance to ask questions back to the computer.")
    greet(player)
    
    def answer():
        q1 = input("""Great! What topic would you like? 
[1] Baseball. 
[2] Geography.
[3] Return to menu. 
""")
        if q1 == "1":
            print("You selected Baseball.")
            a1 = input("""Question 1: How many different pitchers have thrown 20 or more strikeouts in a 9 inning game?
[1] 3
[2] 4
[3] 5
[4] 6 
""")
            if a1 == "1":
                print(f"That is correct! {player}, you get a point!")
                global points
                points = points + 1
            else:
                print(f"{player}, that was incorrect! You get no points!")
            a2 = input("""How many consequitive allstar games did Carl Ripken Jr. play in?
[1] 17
[2] 19
[3] 24
[4] 25
""")
            if a2 == "2":
                print(f"That is correct! {player}, you get a point!")
                points = points + 1
            else:
                print(f"{player}, that was incorrect! You get no points!")
            a3 = input(""" Which Cubs player holds the record for most home runs in a rookie year?
[1] Kris Bryant
[2] Ernie Banks
[3] Ryne Sandberg
[4] Patrick Wisdom
""")
            if a3 == "4":
                print(f"That is correct! {player}, you get a point!")
                points = points + 1
            else:
                print(f"{player}, that was incorrect! You get no points!")
        if q1 == "2":
            print("You selected Geography.")
            a_1 = input("""Question 1: What river passes through the most different countries in the world?
[1] The Nile
[2] The Danube
[3] The Congo
[4] The Niger
""")
            if a_1 == "2":
                print(f"That is correct! {player}, you get a point!")
                points = points + 1
            else:
                print(f"{player}, that was incorrect! You get no points!")
            
            a_2 = input("""Question 2: How many countries does Ukraine border?
[1] 5
[2] 6
[3] 7
[4] 8
""")
            if a_2 == "3":
                print(f"That is correct! {player}, you get a point!")
                points = points + 1
            else:
                print(f"{player}, that was incorrect! You get no points!")
            a_3 = input("""Question 3: What is Uzbekistan's top export?
[1] Gold
[2] Yarn
[3] Petroleum Gas
[5] Alumium
""")
            if a_3 == "1":
                print(f"That is correct! {player}, you get a point!")
                points = points + 1
            else:
                print(f"{player}, that was incorrect! You get no points!")
    
    def ask(q_1: int) -> int:
        global points
        ask_points = points
        if q_1 == 1:
            understood = False
            while not understood:
                kurt_russle = int(input(f"""{player}, you selected to ask a question about Kurt Russell. Which question would you like to ask?
[1] During the filming of which movie did Kurt Russell smash a $40,000 guitar?
[2] Which sport did Kurt Russell want to persue professionally before a career ending injusry?
"""))
                if kurt_russle == 1:
                    print("'I'm an expert on Kurt Russell. I will definitely get this right! The Hateful Eight!' The computer gets 100 points. You lose a point.")
                    ask_points = ask_points - 1
                    global opp_points
                    opp_points = opp_points + 100
                    understood = True
                    print("Your points:")
                    print(ask_points)
                    print("Computer's points:")
                    print(opp_points)
                elif kurt_russle == 2:
                    print("'I'm an expert on Kurt Russell. I will definitely get this right! Baseball!' The computer gets 100 points. You lose a point.")
                    ask_points = ask_points - 1
                    opp_points = opp_points + 100
                    print("Your points:")
                    print(ask_points)
                    print("Computer's points:")
                    print(opp_points)
                    understood = True  
                else:
                    print("I don't understond, try again")
        elif q_1 == 2:
            understood = False
            while not understood:
                royal_families = int(input(f"""{player}, you selected to ask a question about Royal Families. Which question would you like to ask?
[1] What is the name of the dynasty ruling in Morocco
[2] At the end of which conflict did the Valois dynasty end it's reign in France
"""))
                if royal_families == 1:
                    print("'I'm an expert on Royal Families! I will definitly get this right! The Alaouite!' The computer gets 100 points. You lose a point.")
                    ask_points = ask_points - 1
                    opp_points = opp_points + 100
                    understood = True
                    print("Your points:")
                    print(ask_points)
                    print("Computer's points:")
                    print(opp_points)
                elif royal_families == 2:
                    print("'I'm an expert on Royal Families! I will definitly get this right! The War of Three Henry's' The computer gets 100 points. You lose a point.")
                    ask_points = ask_points -1
                    opp_points = opp_points + 100
                    print("Your points:")
                    print(ask_points)
                    print("Computer's points:")
                    print(opp_points)
                    understood = True  
                else:
                    print("I don't understond, try again")
        elif q_1 == 3:
            understood = False
            while not understood:
                italy = int(input(f"""{player}, you selected to ask a question about Italy. Which question would you like to ask?
[1] Who was the first prime minister of the Kingdom of Italy?
[2] What is Italy's largest export?
"""))
                if italy == 1:
                    print("'Uh oh, I don't know anything about Italy. I'll have to guess...")
                    choice_1 = random.randint(1,4)
                    if choice_1 == 1:
                        print("'I guess Camillo Benso!' The computer guessed right! The computer gets 100 points. You lose a point.")
                        ask_points = ask_points - 1
                        opp_points = opp_points + 100
                    elif choice_1 == 2:
                        print("'I guess Guiseppe Garibaldi!' The computer guessed wrong! The computer looses 100 points. You get a point.")
                        ask_points = ask_points + 1
                        opp_points = opp_points - 100
                    elif choice_1 == 3:
                        print("'I guess Victor Emmanuel!' The computer guessed wrong! The computer looses 100 points. You get a point.")
                        ask_points = ask_points + 1
                        opp_points = opp_points - 100
                    elif choice_1 == 4:
                        print("'I guess Guiseppe Mazzini!' The computer guessed wrong! The computer looses 100 points. You get a point.")
                        ask_points = ask_points + 1
                        opp_points = opp_points - 100
                    understood = True
                    print("Your points:")
                    print(ask_points)
                    print("Computer's points:")
                    print(opp_points)
                elif italy == 2:
                    print("'Uh oh, I don't know anyting about Italy. I'll have to guess...'")
                    choice_2 = random.randint(1,4)
                    if choice_2 == 1:
                        print("'I guess packaged medicaments!' The computer guessed right! The computer gets 100 points. You lose a point.")
                        ask_points = ask_points - 1
                        opp_points = opp_points + 100
                    elif choice_2 == 2:
                        print("'I guess car parts!' The computer guessed wrong! The computer looses 100 points. You get a point.")
                        ask_points = ask_points + 1
                        opp_points = opp_points - 100
                    elif choice_2 == 3:
                        print("'I guess refined petroleum!' The computer guessed wrong! The computer looses 100 points. You get a point.")
                        ask_points = ask_points + 1
                        opp_points = opp_points - 100
                    elif choice_2 == 4:
                        print("'I guess valves!' The computer guessed wrong! The computer looses 100 points. You get a point.")
                        ask_points = ask_points + 1
                        opp_points = opp_points - 100
                    print("Your points:")
                    print(ask_points)
                    print("Computer's points:")
                    print(opp_points)
                    understood = True  
                else:
                    print("I don't understond, try again")
        return ask_points
                    
    understood = False
    while not understood:
        global points
        menu = int(input(f"""You have {points} points. The computer has {opp_points} points. What would you like to do next? 
[1] Answer questions.
[2] Ask questions.
[3] Quit and see your points.
"""))
        if menu == 1:
            answer()
            understood = False
        elif menu == 2:
            print("You have selected to ask the computer questions. You will have the option between two questions in three different catagories")
            q1 = int(input("""Which catagory of question would you like to ask about?
[1] Kurt Russell
[2] Royal Families
[3] Italy
[Any other number] Return to menu
"""))
            if q1 == 1:
                points =  ask(1)
            if q1 == 2:
                points =  ask(2)
            if q1 == 3:
                points =  ask(3)
        elif menu == 3:
            if points > opp_points:
                print(f"You finished with {points} points. The computer finished with {opp_points} points. You win! " + THUMBSUP)
            if points < opp_points:
                print(f"You finished with {points} points. The computer finished with {opp_points} points. You Loose! " + THUMBSDOWN)
            if points == opp_points:
                print(f"You finished with {points} points. The computer finished with {opp_points} points. It's a tie! " + SHRUG)
            understood = True
            
        else:
            print("I don't understond, try again")


if __name__ == "__main__":
    main()