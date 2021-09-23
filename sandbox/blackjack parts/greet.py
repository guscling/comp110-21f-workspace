def main():
    def greet(name) -> None: 
        name = None
        global player
        player = input("What is your name? ")
        print("Hello, " + player + ", how are you? In this program you will play the card game blackjack. The suits will be signified with the symbols and the value of the card with the number or word")
    greet(player)