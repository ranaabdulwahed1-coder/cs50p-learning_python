while True:
    try:
        x, y = input('fraction: ').split('/')
        x, y = int(x), int(y)
        percent = round(x/y * 100)
        if percent >= 99:
            print('F')
        elif percent <= 1:
            print('E')
        else:
            print(f'{percent}%')
        break
    except (ValueError, ZeroDivisionError):
        pass
