import random
import pyperclip


def Start():
    print('Options : (R)andom | (E)xit')
    UserInput01 = str(input('Choose an option : '))
    if UserInput01.lower() == 'r':
        Random()
    elif UserInput01.lower() == 'e':
        print('--------------------------------------------------')
        print('Bye!!')
    else:
        print('--------------------------------------------------')
        print('Invalid Option...')


def Random():
    Letters = 'abcdefghijklmnopqrstuvwxyz'
    UpperLetters = Letters.upper()
    LowerLetters = Letters.lower()
    Numbers = '1234567890'
    Symbols = '[](){}=+?|!"#$%&/\\\'*<>,.;:-_'
    global Upper
    Upper = False
    global Lower
    Lower = False
    global Number
    Number = False
    global Symbol
    Symbol = False
    global Weaver
    Weaver = ""
    global Length
    Length = 0
    print('--------------------------------------------------')
    print('Options : (1)Completely Random | (2)Customizable Random')
    UserInput01 = str(input('Choose an option : '))
    if UserInput01 == '1':
        Upper = True
        Lower = True
        Number = True
        Symbol = True
    elif UserInput01 == '2':
        print('--------------------------------------------------')
        UserInput01 = str(input('Include Upper Case? y/n : '))
        if UserInput01.lower() == 'y':
            Upper = True
        elif UserInput01.lower() == 'n':
            Upper = False
        print('--------------------------------------------------')
        UserInput02 = str(input('Include Lower Case? y/n : '))
        if UserInput02.lower() == 'y':
            Lower = True
        elif UserInput02.lower() == 'n':
            Lower = False
        print('--------------------------------------------------')
        UserInput03 = str(input('Include Numbers? y/n : '))
        if UserInput03.lower() == 'y':
            Number = True
        elif UserInput03.lower() == 'n':
            Number = False
        print('--------------------------------------------------')
        UserInput04 = str(input('Include Symbols? y/n : '))
        if UserInput04.lower() == 'y':
            Number = True
        elif UserInput04.lower() == 'n':
            Symbol = False
        print('--------------------------------------------------')
        print('Whats a weaver?, eg. (secure#password) # = weaver, Press enter for non.')
        UserInput05 = str(input('Enter a weaver : '))
        if UserInput05 == "":
            Weaver += ""
        else:
            Weaver += UserInput05
    else:
        print("Invalid Option...")
        Random()

    part2 = True
    while part2:
        print('--------------------------------------------------')
        UserInput02 = int(input('Enter the length of the password : '))
        if UserInput02 <= 0:
            print('--------------------------------------------------')
            print('Minimum Number is 1...')
        if UserInput02 > 50:
            print('--------------------------------------------------')
            print('Maximum number is 50...')
        else:
            Length += int(UserInput02)
            part2 = False
    print('--------------------------------------------------')
    UserInput03 = input('Enter the amount of the password : ')
    Amount = int(UserInput03)

    Password = ""

    if Upper:
        Password += LowerLetters
    if Lower:
        Password += UpperLetters
    if Number:
        Password += Numbers
    if Symbol:
        Password += Symbols
    print('--------------------------------------------------')
    UserInput04 = str(input('Do you want to save the passwords to a file? y/n : '))
    if UserInput04.lower() == 'y':
        UserInput01 = str(input('Enter File Name : '))
        File = open(UserInput01, "a")
        print('--------------------------------------------------')
        UserInput14 = str(input("Do you want a copy to clip board option? y/n : "))
        if UserInput14.lower() == 'y':
            for x in range(Amount):
                Passwords = Weaver.join(random.sample(Password, Length))
                print(f'"  {Passwords}  "  | Password {x + 1} / {Amount}')
                print('--------------------------------------------------')
                UserInput01 = str(input('Copy to clipboard? y/n : '))
                if UserInput01.lower() == 'y':
                    File.write(f'{Passwords}\n')
                    pyperclip.copy(Passwords)
                    print('--------------------------------------------------')
                    print('Copied to clipboard')
                else:
                    File.write(f'{Passwords}\n')
                    pass
        else:
            for x in range(Amount):
                Passwords = Weaver.join(random.sample(Password, Length))
                print('--------------------------------------------------')
                print(f'"  {Passwords}  "  | Password {x + 1} / {Amount}')
                File.write(f'{Passwords}\n')

        print('--------------------------------------------------')
        File.close()
        Start()
    else:
        print('--------------------------------------------------')
        UserInput14 = str(input("Do you want a copy to clip board option? y/n : "))
        if UserInput14.lower() == 'y':
            for x in range(Amount):
                Passwords = Weaver.join(random.sample(Password, Length))
                print(f'"  {Passwords}  "  | Password {x + 1} / {Amount}')
                print('--------------------------------------------------')
                UserInput01 = str(input('Copy to clipboard? y/n : '))
                if UserInput01.lower() == 'y':
                    pyperclip.copy(Passwords)
                    print('--------------------------------------------------')
                    print('Copied to clipboard')
                else:
                    pass
        else:
            for x in range(Amount):
                Passwords = Weaver.join(random.sample(Password, Length))
                print('--------------------------------------------------')
                print(f'"  {Passwords}  "  | Password {x + 1} / {Amount}')

        print('--------------------------------------------------')
        Start()

print(
    '--------------------DISCLAIMER--------------------\nThis is a random and secure password generator use\nthis at your own risk, this was created so i could\nunderstand how a strong and secure password could\nbe created and added my own twist to it ENJOY !!.\nhttps://github.com/NotReeceHarris\n-----------------Coded By ReeceH------------------')
Start()
