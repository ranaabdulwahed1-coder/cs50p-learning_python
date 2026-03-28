import inflect
p = inflect.engine()
names = []
while True:
    try:
        name = input('name  ').title()
        names.append(name)
    except EOFError:
        break
print(f'Adieu, Adieu, too {p.join(names)}')


