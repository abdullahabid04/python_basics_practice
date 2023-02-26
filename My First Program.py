import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number : "))
        if guess < random_number:
            print("Guess again Too low")
        elif guess > random_number:
            print("Guess again Too high")
    print("You guessed number")

def computer_guess(x):
    low, high = 1, x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} high (H), low (L), or correct (C) ').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
        else:
            guess = guess
    print("Computer guessed number")

while 1:
    print("Computer Turn to give you a number")
    guess(10)
    print("Your turn to give computer a number")
    computer_guess(10)
