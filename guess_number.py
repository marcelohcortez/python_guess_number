import random

def guess_number():
    print('\nFor this game you must set a low number and a high number.\nThe computer will try to guess the chosen number using those two as parameters.\n')
    low = int(input('Please select a LOW number and press \'enter\': '))
    high = int(input('Please select a HIGH number and press \'enter\': '))
    answer = ''
    while answer != 'c':
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low  
        answer = input(f'Is the number {computer_guess}?\nPress (H) if it\'s too high\nPress (L) if it\'s too low\nPress (C) if it\'s correct\n ').lower()
        if answer == 'h':
            high = computer_guess - 1
        elif answer == 'l':
            low = computer_guess + 1

    print(f'The number you\'ve chosen is {computer_guess}.\n\n')

guess_number()