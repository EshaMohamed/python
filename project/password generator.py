import random
import string
character=string.ascii_letters + string.digits
def generative_password():
    while True:
        try:
            lenght=int(input("enter the password generator : "))
            if lenght>0:
                break
            else:
                print("pls enter the valid pass")
        except:
            print("invalid so pla try again")
    password=""
    for _ in range(lenght):
        random_char=random.choice(character)
        password+=random_char
    print("============================================")
    print(password)
    print("============================================")
generative_password()