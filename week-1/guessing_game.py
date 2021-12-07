from random import randint
from IPython.display import clear_output
guessed = False
guess_count = 0
computer_guess = randint(0,100)
while not guessed:
    my_guess = int(input ("enter your guess ? "))
    guess_count =  guess_count + 1
    if my_guess > computer_guess :
        print ("Go fish .. Lower")
        guessed = False
    elif my_guess < computer_guess:
        print (" Go fish .. Higher")
        guessed = False
    else:
        if guess_count < 3 :
            print("WOW ! You guessed correctly in " + str(guess_count) + " attempts")
        else:
            print("You guessed correctly in " + str(guess_count) + " attempts")
        guessed = True

