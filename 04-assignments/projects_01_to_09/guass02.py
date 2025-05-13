
import random

def guess(x):
  random_number = random.randint(1,x)
  guess = 0

  while guess != random_number:
    guess = int(input(f'Guess a number between 1 and {x}: '))

    if guess < random_number:
      print('Sorry, guess again. Too low\n.')
    elif guess > random_number:
      print('Sorry, guess again. Too high\n.')
  print(f"Yay, congrats you have guessed the number {random_number}")

guess(10)
# Guess a number between 1 and 10: 5
# Sorry, guess again. Too low
# .
# Guess a number between 1 and 10: 4
# Sorry, guess again. Too low
# .
# Guess a number between 1 and 10: 8
# Sorry, guess again. Too high
# .
# Guess a number between 1 and 10: 7
# Yay, congrats you have guessed the number 7