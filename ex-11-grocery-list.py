grocery_list = []
count = cont = 0


while True:
    question = str(input("\nWhat would you like to do?\n Please enter:\n[P] to print list\n[A] to add an item\n[R] to remove an item\n> ")).upper()
    if question == "A":
        item = str(input("What item would you like to add?\n> "))
        grocery_list.append(item)
        count += 1
        while True:
            question2 = str(input("Would you like to add another one?\n> "))
            if question2 == "yes":
                item = str(input("What item would you like to add?\n> "))
                grocery_list.append(item)
                count += 1
            elif question2 == "no":
                for grocery in grocery_list:
                    cont += 1
                    print(f"{cont}.{grocery}")
                break
    elif question == "P":
        for grocery in grocery_list:
            print(f"{cont}.{grocery}")
        if len(grocery_list) <= 0:
            print("There is nothing here yet.")
    elif question == "R":
        for grocery in grocery_list:
            
            print(f"{cont}.{grocery}")
        remove = str(input("What item would you like to remove?\n>"))
        if remove in grocery_list:
            grocery_list.remove(remove)
                
