import random
def try_me():
    number = random.randint(1, 3)
    if number == 1:
        return ('hello pretty face')
    elif number == 2:
        return ('wanna grab a coffe?')
    else:
        return ('you sound like a donkey.')

if __name__ == "__main__":
    output = try_me()
    print(output)