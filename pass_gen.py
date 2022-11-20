import random


print('Welcome to Password Generator Wizard!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = int(input("How many 'passwords' do you want us to generate?"))

length = int(input('Please let us know the length of the password!'))

print('\nHere you go!')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)






