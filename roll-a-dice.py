import random

no = 'y'

while no == 'y':
    number = random.randint(1, 6)
    input_1 = input("Enter 'y' to roll a dice and 'q' to exit : ")
    if input_1 == 'y':
        if number == 1:
            print('[-----]')
            print('[     ]')
            print('[  0  ]')
            print('[     ]')
            print('[-----]')
        if number == 2:
            print('[-----]')
            print('[     ]')
            print('[0   0]')
            print('[     ]')
            print('[-----]')
        if number == 3:
            print('[-----]')
            print('[     ]')
            print('[0 0 0]')
            print('[     ]')
            print('[-----]')
        if number == 4:
            print('[-----]')
            print('[0   0]')
            print('[     ]')
            print('[0   0]')
            print('[-----]')
        if number == 5:
            print('[-----]')
            print('[0   0]')
            print('[  0  ]')
            print('[0   0]')
            print('[-----]')
        if number == 6:
            print('[-----]')
            print('[0   0]')
            print('[0   0]')
            print('[0   0]')
            print('[-----]')
    elif input_1 == 'q':
        exit()
