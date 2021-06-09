import random
import string
from time import sleep

letters = list(string.ascii_letters)
symbols_nums = list(string.digits) + list(string.punctuation)
available_chars = letters + symbols_nums

print('Welcome to PyPass - the Python Password Generator!')


def password_generator():
    while True:
        try:
            num_chars = int(input('\nHow long should your password be? Enter a number between 5 and 30: '))
            if num_chars < 5 or num_chars > 30:
                raise ValueError
        except ValueError:
            print('\nERROR: Invalid Entry - Only values between 5 and 30 are accepted.\n')
        else:
            break

    password = ''
    for char in range(num_chars):
        password += random.choice(available_chars)

    print('\n' + password)

    while True:
        try:
            another_pass = input('\nCreate another password? (Y)es or (N)o: ').lower()
            if another_pass[0] != 'y' and another_pass[0] != 'n':
                raise ValueError
        except ValueError:
            print("\nERROR: Invalid Entry - Only 'Y' and 'N' are recognized.")
        else:
            if another_pass[0] == 'y':
                password_generator()
            else:
                print('\nThanks for using PyPass! The program will now quit.')
                sleep(3)
                exit()


password_generator()
