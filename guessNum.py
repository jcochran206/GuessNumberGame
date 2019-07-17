#############################
# Title: Guess my Number Game
# created by Jonathan Cochran
# date 17 July 2019
#############################

import random
# Greeting
print("Hello. What is your name?")
name = input()
# random Number generated
secretNum = random.randint(1, 20)
print('Well ' + name + ' I am thinking of a number between 1 thru 20?')

# ask player limited amount of times ex 6
for guessTaken in range(1, 7):
    print('Take a guess')
    guess = int(input()) # input must be turned in to number
    if guess > secretNum:
        print('your guess is too high')
    elif guess < secretNum:
        print('your guess is too low')
    else:
        break # the condition is met

if guess == secretNum:
    print('GOOD job! ' + name + 'You guessed the right number in ' + str(guessTaken) + '!')
else:
    print('Nope.  The number is ' + str(secretNum) + ' and you have exceeded your tries.  better luck next time' + name + ' .')
