import random

print("Welcome to the random number game!")
print("Enter your name: ")
name = input()
print("Hello " + name + "! Guess a number 1-20: ")


def numberGuess():
    correctnumber = random.randrange(1, 20)
    guess = input()
    guessint = int(guess)



    if correctnumber == guessint:
        print("You got the correct number! Play again? Y or N.")
        playagain = input()

        if playagain == "Y":
            numberGuess()



    else:
        print("This was not the right number. Try again!")
        numberGuess()



numberGuess()