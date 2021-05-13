# Importing random built-in module to generate a random number --> by Sohan
import random

# Printing the heading of the game --> by Sohan
print("Number Guessing Game by Sohan !")

# Generating the random number using randit() function --> by Sohan
generatedNumber = random.randint(1,9)

# Initializing the chances variable by 0 --> by Sohan
chances = 0

# Printing to tell the user to guess a number --> by Sohan
print("Guess a number (between 1 and 9):")

''' Running while loop when chances < 5 to check if user entered the
 correct or wrong number --> by Sohan '''

while chances < 5:
    # Saving the input value as a integer in a variable --> by Sohan
    guessedNumber = int(input("Enter your guess! :- "))

    # Printing Greetings if generated number is same as inputed value --> by Sohan
    if (guessedNumber == generatedNumber):
        print("Congrats! You WON the CHALLENGE !!")
        break
    
    # Printing hint if inputed value is less than generated value --> by Sohan
    elif(guessedNumber < generatedNumber):
        print("Your guess was too low: Guess a number higher than", guessedNumber)

    # Printing hint if inputed value is higher than generated value --> by Sohan
    else:
        print("Your guess was too high: Guess a number lower than", guessedNumber)

    # Increasing chances each time by 1 --> by Sohan
    chances += 1

# Printing 'You Lose' if chances are greater than 5
if not chances < 5:
    print("You lose !!!! The number is ",generatedNumber)            