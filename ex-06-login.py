# login program
def login(username: str, password: str) -> bool:
    is_authenticated = False
# define username and password
    if username == "admin" and password == "1234":
        is_authenticated = True

    return is_authenticated
# ask user for username and password
user = input("Username: ")
passw = input("Password: ")

attempt = 1
# user gets 5 tries
max_attempts = 5
is_authenticated = False

while login(user, passw) == False:
    attempt += 1
    # define numbers of tries
    if attempt > max_attempts: break
    # break terminates the loop
    print("Login failed, re-enter your credentials.")

    user = input("Username: ")
    passw = input("Password: ")
else:
    is_authenticated = True
    print("Login successful")

if not is_authenticated:
    print("Your account has been temporarily locked.")

