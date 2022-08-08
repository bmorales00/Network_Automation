
"""
database = {"Juan": "123", "Joe": "MJ123"}
attempts = 0
while attempts < 3:
    userName = input("Enter a Username here: ")
    userPass = input("Enter a Password here: ")
    if userName in database.keys() and userPass == database.get(userName):
        print(f'Welcome back {userName}')
        break
    elif userName in database.keys() and userPass != database.get(userName):
        print(f'This is the wrong password, Please try again! ')
        attempts += 1
    else:
        print("yes")


    else:
        #key = input()
        #answer = input()
        #new_user = input()
        #new_pass = input()
        key = input()
        while key != "q":
            print(f'This user does not exist!, Would you like to create one? [Y] or [N]?: {answer}')
            answer = input()
            if answer is "Y" or "y":
                print(f'Create a Username: {new_user}')
                print(f'Create a Password {new_pass}')
                print(f'Succesfully created a new account')
                database.update(new_user = new_pass)
            elif answer is "N" or "n":
                break
            else:
                print(f'Please press q to quit {key}')

"""

database = {"Juan": "123", "Joe": "MJ123"}
attempts = 0
while attempts < 3:
    userName = input("Enter a Username here: ")
    userPass = input("Enter a Password here: ")
    if userName in database.keys() and userPass == database.get(userName):
        print(f'Welcome back {userName}')
        break
        if userPass != database.get(userName):

            print(f'This is the wrong password, Please try again! ' )

        else:
            print(f'You are Locked out')

    else:
        print("yes")