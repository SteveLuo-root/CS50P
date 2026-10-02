import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

random_num = random.randint(1, n)

while True:
    try:
        guess_num = int(input("Guess: "))
        if guess_num <= 0:
            continue
        if guess_num < random_num:
            print("Too small!")
        elif guess_num > random_num:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
