# How the game works:
# The user enters a number and the computer another. 
# The two numbers entered are added together. 
# The user tries to guess whether the sum of the numbers will be odd or even.
# If the user gets it right, user wins. If not, the computer wins.
print("-=-" * 15)
print("THE ODD OR EVEN GAME")  
print("-=-" * 15)
# get random numbers from the library
from random import randint
count = 0
while True:
    # ask user to input a number 
    user = int(input("Enter a number: "))
    # computer will choose its number between 0 and 10
    computer = randint(0, 11)
    # sum of user's number and computer's number
    total = user + computer
    choice = " "
    # ask user to choose between even or odd
    while choice not in "EO":
        choice = str(input("Do you choose odd or even? [O/E]\n>")).upper().strip()
    # inform the output to user
    print(f"You chose number {user} and the computer chose number {computer}. The sum of both is {total}.")
    # find if the sum of user's number and computer's number equals to an odd or even number
    print("It's an EVEN number." if total % 2 == 0 else "It's an ODD numebr.")
    # count the wins
    if choice == "E":  
        if total % 2 == 0:
            print("You WIN!")
            count += 1
        else:
            print("You LOST!")
            break
    elif choice == "O":
        if total % 2 == 1:
            print("You WIN!")
            count += 1
        else:
    # inform user how many wins at the end
            print(f"GAME OVER! You won {count} times.")
            break
    print("----" * 15)  
    
    