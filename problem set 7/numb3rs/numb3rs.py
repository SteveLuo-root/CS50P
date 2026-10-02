import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if not matches:
        return False
    for number in matches.groups():
        if len(number) > 1 and number.startswith("0"):
            return False
        num = int(number)
        if num > 255:
            return False
    return True


if __name__ == "__main__":
    main()
