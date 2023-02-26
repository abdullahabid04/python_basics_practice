import random
import sys

choice, num1, num2, answer, right, rightans, wrongans, operator = 0, 0, 0, 0, 0, 0, 0, ''

while 1:
    num1, num2, choice = random.randint(1, 10), random.randint(1, 10), random.randint(1, 4)
    if choice == 1:
        operator = '+'
        right = num1 + num2
    if choice == 2:
        operator = '-'
        right = num1 - num2
    if choice == 3:
        operator = '*'
        right = num1 * num2
    if choice == 4:
        operator = '/'
        right = num1 // num2
    answer = int(input(f'{num1} {operator} {num2} : '))
    if answer != right:
        print("You entered the wrong answer")
        wrongans += 1
    else:
        print("You entered the right answer")
        rightans += 1
    if wrongans == 3:
        print("You lose")
        sys.exit(1)
