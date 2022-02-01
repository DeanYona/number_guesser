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


def difference(guess):
    if guess > comp_num:
        return guess - comp_num
    else:
        return comp_num - guess

def bigger_lower(guess):
    if guess > comp_num:
        return("pick a smaller number")
    else:
        return("pick a larger number")

def even_uneven(guess):
    if comp_num % 2 == 0:
        return("the number is even")
    else:
        return("the number is uneven")

def close_far(guess):
    dif = difference(guess)
    if dif < 10:
        return("you are very close")
    elif dif < 30:
        return("you are pretty close")
    else: 
        return("you are not close at all")

class HintSet:
    def __init__(self):
        self.hint_makers = [bigger_lower, even_uneven, close_far]

    def get_hint(self, guess):
        hint_maker = random.choice(self.hint_makers)
        if hint_maker is even_uneven:
            self.hint_makers.remove(even_uneven)
        return hint_maker(guess)

hs = HintSet()

def logic():
    while True:
        tries = 5
        while tries > 0:
            tries -= 1
            user_num = user()
            if user_num == comp_num:
                print("you win")
                break
            else:
                if tries == 0:
                    print("you lose")
                    break
                hint = hs.get_hint(user_num)
                print(hint)

        if tries == 0:
            print("the number is %d" % comp_num)

        play_again = input("play again?")
        if play_again != "yes":
            break
    
logic()