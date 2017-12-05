#This is the first program
import random
number = random.randint(1,25)
while 1:
    guess = input("Guess the number: ")
    if number == guess:
        print("you guess it right")
        break
    if number < guess:
        qut = str(raw_input("too high, want to try again: Y/N "))
    if number > guess :
        qut = str(raw_input("too less, want to try again: Y/N "))
    if qut != 'Y' and qut != 'y':
        break



