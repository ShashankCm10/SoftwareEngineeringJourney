secret=7
guess=int(input("Guess the number between 1 and 10: "))
while guess!= secret:
    if guess<secret:
        print("Too low, try again")
    else:
        print("Too high, try again")
    guess=int(input("Guess the number between 1 and 10: "))
if guess==secret:
    print("Congratulations! You guessed the number.")