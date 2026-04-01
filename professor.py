import random
def main():
    score = 0
    level = get_level()
    for s in range(10):
        if get_integer(level):
            score = score + 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

#create the equation based on level chosen
def get_integer(level):
    if level == 1:
        min_num = 0
        max_num = 9
    elif level == 2:
        min_num = 10
        max_num = 99
    else:
        min_num = 100
        max_num = 999
# gen random numbers
    x = random.randint(min_num, max_num)
    y = random.randint(min_num, max_num)
    try:
        for i in range(3):
            answer = int(input(f'{x} + {y} = '))
            if answer == x + y:
                return True
        else:
            print('EEE')
    except ValueError:
            print('EEE')
    print(f'{x} + {y} = {x+y}')
    return False

if __name__ == '__main__':
    main()

