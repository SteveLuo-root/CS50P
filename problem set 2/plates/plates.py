def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if start(s) and length(s) and numbers(s) and other(s):
        return True
    else:
        return False

def start(s):
    if len(s) >= 2 and s[:2].isalpha():
        return True
    else:
        return False

def length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def numbers(s):
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            return s[i:].isdigit()
    return True

def other(s):
    return s.isalnum()

main()
