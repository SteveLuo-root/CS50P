name = input("camelCase: ")

for c in name:
    if c.isupper():
        print("_" + c.lower(), end='')
    else:
        print(c, end='')

print()
