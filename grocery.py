g = {}
while True:
    try:
        item = input().lower()
        g[item] = g.get(item, 0) + 1
    except EOFError:
        break
for item in sorted(g):
    print(g[item], item)
