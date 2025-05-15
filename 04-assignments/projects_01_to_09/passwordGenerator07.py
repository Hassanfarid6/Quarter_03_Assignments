import random

print('Welcome To Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890'

number = int(input('Amount of passwords To Generate :'))
lenght = int(input('Enter your password lenght :'))

print('\nHere are your passwords\n')
for password in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)