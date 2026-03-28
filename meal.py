
def main():
    time = input('what time is it? ')
    hours = convert(time)

    if 7.0 <= hours <= 8.0:
        print('breakfast time!!')
    elif 12.0 <= hours <= 13.0:
        print('lunch time!!')
    elif 18.0 <= hours <= 19.0:
        print('dinner')
    else:
        print('Not meal time')

def convert(time):
    hours, minutes = time.split(':')
    return int(hours) + int(minutes) / 60

main()

