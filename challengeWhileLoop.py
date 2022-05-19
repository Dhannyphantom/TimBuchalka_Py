import random

print("Welcome to the Guessing game by python")
print("Select a difficulty of 1 - 1000000")
maxNumber = int(input())

answer = random.randint(1, maxNumber)
print("Please guess a number between 1 and {}".format(maxNumber))

result = int(input())
counter = 1

while result != answer:
    if counter >= 10:
        print("Game Over, the number was {}".format(answer))
        break
    counter += 1
    if result > answer:
        print("Guess Lower")
        result = int(input())
    else:
        print("Guess Higher")
        result = int(input())
else:
    if counter == 1:
        print("You got it the first try")
    else:
        print("You guessed correctly in {} tries".format(counter))
