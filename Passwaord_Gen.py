import string
import random

char = list(string.ascii_letters + string.digits + "@")

def generate_pass():
    password_length = int(input("What will be the Length of you Password : "))
    random.shuffle(char)

    password = []
    for x in range(password_length):
        password.append(random.choice(char))
    
    random.shuffle(password)
    password = "".join(password)
    print("Here is your new Password : ", password)


option = input("Do you want to have a new secured Password ? Y/N : " )

if option == "Y" or option == "y":
    generate_pass()
elif option == "N" or option == "n":
    print("Program Ended")
    exit()
else: 
    print("Invalid input")
    exit()