print("=-=" * 20)
print("                    Your Grocery List")
print("=-=" * 20)

# create an empty list to store the groceries
grocery_list = []
count = 0

while True:
    # create a main menu and ask user to choose an option
    question = str(input("\nWhat would you like to do?\n Please enter:\n[A] to add an item to the list\n[P] to print the list\n[R] to remove an item from the list\n[D] to be done with your list\n> ")).upper()
    if question == "A":
        item = str(input("What item would you like to add?\n> ")).upper()
    # after user input the item, add it to grocery_list
        grocery_list.append(item)
        count += 1
        while True:
            question2 = str(input("Would you like to add another one? [YES/NO]\n> ")).upper()
            if question2 == "YES":
                item = str(input("What item would you like to add?\n> ")).upper()
                grocery_list.append(item)
                count += 1
            elif question2 == "NO":
        # enumerate each item in the grocery_list, starting from 1, then print it
                for position, name in enumerate(grocery_list, start=1):
                    print(f"\n{position}.{name}")
                print("\nThanks for shooping.")
                print("=-=" * 20)
        # break the loop if user inputs no and send back to the main menu
                break
    elif question == "P":
        for position, name in enumerate(grocery_list, start=1):
            print(f"\n{position}.{name}")
        print("\nThanks for shooping.")
        print("=-=" * 20)
        # if user wants to print and there is no item on the list, inform user
        if len(grocery_list) <= 0:
            print("\nThere is nothing here yet. Start shopping :)")
    elif question == "R":
        for position, name in enumerate(grocery_list, start=1):
            print(f"\n{position}.{name}")
        print("\nThanks for shooping.")
        print("=-=" * 20)
        remove = str(input("What item would you like to remove?\n> ")).upper()
        # check if the item user input is in the list
        if remove in grocery_list:
            # if yes, remove the item
            grocery_list.remove(remove)
        print("\nThanks for shooping.")
        print("=-=" * 20)
    elif question == "D":
        for position, name in enumerate(grocery_list, start=1):
            print(f"\n{position}.{name}")
        print("\nThanks for shopping. Have an awesome day :) ")
        # if user is done, stop the entire program
        break
                
