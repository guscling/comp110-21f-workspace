SECRET: int = 3
print("Im thinking of a number between 1-5. what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
        print("Correct")
else:
        print("Nope")
print( "Game over")