import random
while True:
    try:
        # turns input to number we can use
        level = int(input('Level: '))
        if level > 0:
            break
        else:
            pass
    #if non int given
    except ValueError:
        pass
number = random.randint(1, level)
while True:
    try:
        guess = int(input('Guess: '))
        if guess == number:
            print('right on!')
            break
        elif guess > number:
            print('lowerr')
        elif guess < number:
            print('higher')
    except ValueError:
        pass


