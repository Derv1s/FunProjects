# Number Guessing Game
import random as rn

number = rn.randint(0,101)
right = 6

print("Try to guess the number between 0 and 100!")
print(f"You have {right} guess right now!")
guess = int(input("Enter is your guess?\n"))

while right >= 1:
    right -= 1

    if right == 0 and guess != number:
        print(f"You have no more guesses!\nNumber was = {number}")
        break

    if guess > number:
        print("down!")
        print(f"You have {right} guess left!")
        guess = int(input("Enter is your guess?\n"))

    elif guess < number:
        print("up!")
        print(f"You have {right} guess left!")
        guess = int(input("Enter is your guess?\n"))

    elif guess == number:
        print("You found the number!")
        break