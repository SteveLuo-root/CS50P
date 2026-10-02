groceries = {}

while True:
    try:
        item = input().upper()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except EOFError:
        print()
        break

for item in sorted(groceries):
    print(groceries[item], item)
