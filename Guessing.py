import random

def print_hi(*players):
    # Use a breakpoint in the code line below to debug your script.

    print(players[0], "VS", players[1], ", first to guess the hidden number wins")  # Press ⌘F8 to toggle the breakpoint.
    print("The only rule is, anytime you lose, your opponent gets a hint. \nENJOY! \n \n")



def make_a_guess(guess):
    print("Making a guess of", guess)
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    player1 = input("Player1, Enter your name: ")
    player2 = input("Player2, Enter your name: ")

    print_hi(player1, player2)
    target = random.randint(1, 100)
    guess = 0
    highest = 100
    lowest = 1
    #print("Target is:", target)

    isPlayer1 = False
    player = ""
    while target != guess:
        isPlayer1 = not isPlayer1
        if isPlayer1 == True:
            player = player1
        else:
            player = player2

        if highest > guess > target:
            highest = guess
        elif lowest < guess < target and guess != 0:
            lowest = guess
        if guess == 0:
            guess = int(input(f"{player}, Guess a number between 1 to 100: "))
        elif target < guess:
            guess = int(input(f"{player}, Guess a lower number, Try between {lowest} to {highest}: "))
        else:
            guess = int(input(f"{player}, Guess a higher number, Try between {lowest} to {highest}: "))
    print(f"{player}, You won!")








