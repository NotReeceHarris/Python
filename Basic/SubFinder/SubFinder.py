import requests
import time


# ----------------------------------------- Beginning of start
def start():
    print('Example : \'subtest.perm\', (no \'www.\' or \'https://\')')
    UserInput01 = str(input('Enter the url you want to scan : '))
    DomainTest = 'http://www.' + UserInput01
    try:
        request = requests.get(DomainTest)
        if request.status_code == 200:
            options = True
            while options:
                print('--------------------------------------------------')
                print('Options : \'Q\'uick Scan | \'M\'edium Scan | \'A\'dvanced Scan | \'F\'ull Scan')
                UserInput02 = str(input('What scan do you want to preform? : '))
                if UserInput02.lower() == 'q' or UserInput02.lower() == 'm' or UserInput02.lower() == 'a' or UserInput02.lower() == 'f':
                    print('--------------------------------------------------')
                    print('This may take a while...')
                    DomainNext = UserInput01.lower()
                    OptionNext = UserInput02.lower()
                    Step2(DomainNext, OptionNext)
                    options = False
                else:
                    print('--------------------------------------------------')
                    print('Invalid option...')

    except requests.ConnectionError:
        print('--------------------------------------------------')
        print(f'{UserInput01}, doesn\'t exist please check again.')
        start()


# ----------------------------------------- Step 2
def Step2(Domain, Option):
    if Option == 'q':
        print('--------------------------------------------------')
        print('Quick Scan Chosen')
        File = open('01quickscan.txt', 'r')
        Content = File.read()
        SubDomains = Content.splitlines()
        Count = 0
        Start = time.time()
        Found = []
        for SubDomain in SubDomains:
            Url = f'http://{SubDomain}.{Domain}'
            try:
                requests.get(Url)
            except requests.ConnectionError:
                print(f'Not Found. ({Count} / 1000) | {Url}')
                pass
            else:
                print(f'{Url}, Found')
                Found.append(Url)
            Count += 1
        print(Found)
        print(f'There where {Count}, Attempts made in {round(time.time() - Start, 2)}, Seconds/Minutes')
    elif Option == 'm':
        print('--------------------------------------------------')
        print('Medium Scan Chosen')
        File = open('02mediumscan.txt', 'r')
        Content = File.read()
        SubDomains = Content.splitlines()
        Count = 0
        Start = time.time()
        Found = []
        for SubDomain in SubDomains:
            Url = f'http://{SubDomain}.{Domain}'
            try:
                requests.get(Url)
            except requests.ConnectionError:
                print(f'Not Found. ({Count} / 10000) | {Url}')
                pass
            else:
                print(f'{Url}, Found')
                Found.append(Url)
            Count += 1
        print(Found)
        print(f'There where {Count}, Attempts made in {round(time.time() - Start, 2)}, Seconds/Minutes')
    elif Option == 'a':
        print('--------------------------------------------------')
        print('Advanced Scan Chosen')
        File = open('03advancedscan.txt', 'r')
        Content = File.read()
        SubDomains = Content.splitlines()
        Count = 0
        Start = time.time()
        Found = []
        for SubDomain in SubDomains:
            Url = f'http://{SubDomain}.{Domain}'
            try:
                requests.get(Url)
            except requests.ConnectionError:
                print(f'Not Found. ({Count} / 100000) | {Url}')
                pass
            else:
                print(f'{Url}, Found')
                Found.append(Url)
            Count += 1
        print(Found)
        print(f'There where {Count}, Attempts made in {round(time.time() - Start, 2)}, Seconds/Minutes')
    elif Option == 'f':
        print('--------------------------------------------------')
        print('Full Scan Chosen')
        File = open('04fullscan.txt', 'r')
        Content = File.read()
        SubDomains = Content.splitlines()
        Count = 0
        Start = time.time()
        Found = []
        for SubDomain in SubDomains:
            Url = f'http://{SubDomain}.{Domain}'
            try:
                requests.get(Url)
            except requests.ConnectionError:
                print(f'Not Found. ({Count} / 1000000) | {Url}')
                pass
            else:
                print(f'{Url}, Found')
                Found.append(Url)
            Count += 1
        print(Found)
        print(f'There where {Count}, Attempts made in {round(time.time() - Start, 2)}, Seconds/Minutes')


# ----------------------------------------- Start of Script
print(
    '--------------------DISCLAIMER--------------------\nDon\'t use this tool on any website you don\'t have\npermission do to so on this is just to demonstrate\nhow easy it is to do recon on a website.\nhttps://github.com/NotReeceHarris\n-----------------Coded By ReeceH------------------')
start()
