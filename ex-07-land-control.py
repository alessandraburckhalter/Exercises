# Task: Make a program that has a function that takes the dimensions of a rectangular land (width and length) and shows the land area.
print("--" * 20)
print("              LAND CONTROL    ")
print("--" * 20)
# Create a function to calculate the land area
def landArea(width, length):
    times = width * length
    print(f"The land area of {w} x {l} is {times}m.")
# Ask user to input width and length
w = float(input("WIDTH (m): "))
l = float(input("LENGTH (m): "))
# Call function
landArea(w, l)