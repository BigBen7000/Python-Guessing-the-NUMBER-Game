import random
import os

# generates a random number
randNumber = random.randint(1, 100)

userGuess = None
guesses = 0

# clears the screen
os.system('cls')

# loop
while(userGuess != randNumber):
    print("Enter your guess:")
    userGuess = int(input("> "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
