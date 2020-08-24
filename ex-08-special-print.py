# Make a program that has a function called write (), that receives any text as a parameter and shows a message with an adaptive size border

# create a funtion to add border to user's input
def write(msg):
    size = len(msg)
    print("~" * size)
    print(msg)
    print("~" * size)

# ask user to tell you something
while True: 
    write(input('Tell me something: '))

