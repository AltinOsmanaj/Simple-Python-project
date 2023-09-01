from random import randint
import sys
# Generate a number 1-10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# Input from user?
# Check if that input is a number 1-10
while True:
    try:
        guess = int(input('Guess a number 1-10:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('You are a genius!')
                break
        else:
            print('Hey bozo, I said 1-10')
    except ValueError:
        print('Please enter a number')
        continue
