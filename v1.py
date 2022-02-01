import random

# comp_num = 0
user_num = None
# difference = 0

a = 0
b = 100


comp_num = int(random.randrange(a, b))

def user():
    # user_num = None
    while user_num < a or user_num > b:
        global user_num
        user_num = int(input("pick a number from 0 to 100"))


# hints = [bigger or lower, even or uneven, how close you were]

# def bol():
#     if user_num > comp_num:
#         return("pick a smaller number")
#     else:
#         return("pick a larger number")

# def eou():
#     if comp_num % 2 == 0:
#         return("the number is evem")
#     else:
#         return("the number is uneven")

# def hcyw():
#     if difference < 10:
#         return("you are very close")
#     elif difference < 30:
#         return("you are pretty close")
#     else: 
#         return("you are not close at all")

# hints = [bol,eou,hcyw]

# def chosen_hint():
#     hint = random.choice(hints)
#     print(hint)


# if user_num > comp_num:
#     difference = user_num - comp_num
# else:
#     difference = comp_num - user_num


def main():
    tries = 3
    user()
    # if difference == 0:
    #     print("You Win!")
    # else:
    #     print("you got another try")
    #     chosen_hint()
    while user_num != comp_num:
        while tries > 0:
            if user_num > comp_num:
                print("try something smaller")
                user()
            else:
                print("try something bigger")
                user()
            tries -= 1
    
    
