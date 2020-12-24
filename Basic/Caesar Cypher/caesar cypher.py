charlist = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'z',
    23: 'w',
    24: 'q',
    25: 'y',
    26: 'z',
    27: '1',
    28: '2',
    29: '3',
    30: '4',
    31: '5',
    32: '6',
    33: '7',
    34: '8',
    35: '9',
    36: '0',
    34: ',',
    35: '(',
    36: ')',
    37: '!',
    38: '?',
    39: '\'',
    40: '/',
    41: '&'
    }


def encrypt():
    UserInput01 = str(input('Enter a message to encrypt : '))
    while True:
        try:
            UserInput02 = int(input('Enter a offset for encrypt : '))
            if UserInput02 >= 16:
                print('Invalid Input, Between 5 and 15')
            elif UserInput02 <= 4:
                print('Invalid Input, Between 5 and 15')
            else:
                break
        except ValueError:
            print('Invalid Input, Integers Only....')
    for x in charlist:
        print(x)
























def decrypt():
    UserInput01 = str(input('Enter a message to decrypt : '))

UserInport01 = str(input('Options : (E)ncrypt, (D)ecrypt\nWhat module do you want to load? : '))
if UserInport01.lower() == 'encrypt' or 'e':
    encrypt()
elif UserInport01.lower() == 'decrypt' or 'd':
    decrypt()