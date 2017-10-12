'''
Caesar Cipher 1.0

Author: Lucas Barzan from Codenific.com

-This is a simple encrypt/decrypt program based on Caesar Cipher. It is intended only for educational and personal purposes.

-DO NOT use this to encrypt sensitive information.

-It does not support characters like 'é', 'á', 'ã', etc.

'''

def getMode():
    while True:
        mode = input('Enter E for Encrypt or D for Decrypt: ').upper()
        if mode != 'E' and mode != 'D': #Entered mode is neither E nor D
            continue
        else: #Entered mode is E or D and the while loop is broken
            return mode
            break

def getMessage():
    return input('Enter the message: ')

def getKey():
    while True:
        try:
            key = int(input('Enter a key (at least 1 and at most 25): '))
        except ValueError: #If the input can't be converted to int
            print('Key must be an integer')
            continue
        else:
            if 1 <= key <= 25: #The input is an int between 1 and 25
                return key
            else:
                continue

def getNewMessage(mode, message, key):
    from string import ascii_letters
    alphabet = ascii_letters
    new_message = ''
    if mode == 'E':
        for char in message:
            if char.isalpha():
                i = alphabet.find(char) + key
                if i >= 52:
                    i -= 52
                new_message += alphabet[i]
            else:
                new_message += char
    elif mode == 'D':
        for char in message:
            if char.isalpha():
                i = alphabet.find(char) - key
                if i < 0:
                    i += 52
                new_message += alphabet[i]
            else:
                new_message += char
    import time
    time.sleep(1)
    print('{}\n{}\n{}'.format('*' * 70, new_message, '*' * 70))

mode = getMode()
message = getMessage()
key = getKey()
getNewMessage(mode, message, key)
