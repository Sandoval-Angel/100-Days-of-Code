alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(message, shift):
    message_list = list(message)
    encrypted_list = []

    for letter in message_list:
        try:
            encrypted_list.append(alphabet[alphabet.index(letter) + shift])
        except IndexError:
            encrypted_list.append(alphabet[alphabet.index(letter) + shift - 26])
        except ValueError:
            encrypted_list.append(letter)

    print(''.join(encrypted_list))


def decrypt(message, shift):
    message_list = list(message)
    decrypted_list = []

    for letter in message_list:
        try:
            decrypted_list.append(alphabet[alphabet.index(letter) - shift])
        except IndexError:
            decrypted_list.append(alphabet[alphabet.index(letter) - shift - 26])
        except ValueError:
            decrypted_list.append(letter)

    print(''.join(decrypted_list))


while True:
    try:
        encrypt_decrypt = input('Do you want to (e)ncrypt or (d)ecrypt message? ').lower()[0]

        if encrypt_decrypt != 'e' and encrypt_decrypt != 'd':
            raise ValueError
    except ValueError:
        print('Invalid entry!')
    else:
        break

full_message = input('Enter the message: ').lower()

while True:
    try:
        shift_amount = int(input('Enter shift amount (between -25 and 25): '))

        if shift_amount > 25 or shift_amount < -25:
            raise ValueError
    except ValueError:
        print('Invalid entry!')
    else:
        break

if encrypt_decrypt == 'e':
    encrypt(full_message, shift_amount)
elif encrypt_decrypt == 'd':
    decrypt(full_message, shift_amount)

input('')
