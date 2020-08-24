# Task: Make a program that has a function that receives several parameters with integer values. The program has to analyze all the values ​​and say which one is the highest.

# import sleep from library
from time import sleep
# create the function
def higher(* num):
    print('=' * 50)
    print('Analyzing the reported numbers...')
    sleep(1.5)
    # show the reported numbers
    for n in num:
        print(f'{n}', end=' ')
        sleep(0.7)
    # inform how many numbers were reported
    print(f'\n{len(num)} numbers were reported.')
    sleep(1.5)
    # print the highest number reported
    if len(num) != 0:
        print(f'The highest number reported was {max(num)}.')


# main program
higher(1, 2, 3, 4)
higher(4, 2, 5, 9, 0)
higher(0, 8, 3)
higher(7, 6)
higher()