import random

pw_chars = 'abcdefghijklmnopqrstuvwxyz123456789!.,?#$%^&*()'

password_length = input('Password length: ')

def pwGenerator(password_length):
    password = ''
    for i in range(int(password_length)):
        password += random.choice(pw_chars)

    return password

password = pwGenerator(password_length)

print(f'Passord: {password}')