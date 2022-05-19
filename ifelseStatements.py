
# A GUESSING GAME
print("Guess a number between 1 and 10")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Guess Higher")
    else:
        print("Guess Lower")
    guess = int(input())
    if guess == 5:
        print("You guessed it correctly")
    else:
        print("You guessed wrong")
else:
    print("You got it the first time")
