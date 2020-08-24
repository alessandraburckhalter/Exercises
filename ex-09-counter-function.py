# import sleep from the library
from time import sleep

def counter(start, end, step):
# convert negative number to a positive number
    if step < 0:
        step += -1
    if step == 0:
        step = 1
    print("=-=" * 20)
    print(f"Counting from {start} to {end} of {step} in {step}.")
    sleep(2.0)


    if start < end:
        count = start
        while count <= end:
            print(f"{count} ", end=" ", flush=True)
            sleep(0.5)
            count += step
        print("END")
    else:
        count = start
        while count >= end:
            print(f"{count} ", end=" ", flush=True)
            sleep(0.5)
            count -= step
        print("END")

# main program
# define the counter numbers
counter(1, 10, 1)
counter(10, 0, 2)
print("=-=" * 20)
print("Now it's your turn! Personalize your counter.")
# ask user to enter the numbers
s = int(input("Start: "))
e = int(input("End: "))
stp = (int(input("Step: ")))
counter(s, e, stp)


