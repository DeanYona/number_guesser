import random

a = 1
b = 100

comp_num = int(random.randrange(a, b))

def user():
    while True:
        try:
            guess = int(input("pick a number from 1 to 100: "))
            if guess in range(a, b):
                return guess    
                break
        except Exception:
            pass

        print("\nInvalid answer, try again")

def logic():
    tries = 5
    while tries > 0:
        tries -= 1
        user_num = user()
        if user_num == comp_num:
            print("you win")
            break
        if tries == 0:
            print("you lose")
            break
        if user_num > comp_num:
            print("try something smaller")
        elif user_num < comp_num:
            print("try something bigger")

    if tries == 0:
        print("the number is %d" % comp_num)
    
logic()



    

    
