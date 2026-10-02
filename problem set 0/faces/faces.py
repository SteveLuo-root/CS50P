def main():
    text=input("user's input: ")
    print(convert(text))

def convert(t):
    return t.replace(':)', '🙂').replace(':(', '🙁')

main()
