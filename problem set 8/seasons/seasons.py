from datetime import date
import inflect
import sys

def main():
    birthday_str = input("Date of Birth: ")
    strings = convert(birthday_str).capitalize()
    print(f"{strings} minutes")

def convert(birthday_str):
    try:
        birthday = date.fromisoformat(birthday_str)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    diff = today - birthday
    days = diff.days
    minutes = days * 24 * 60

    p = inflect.engine()
    words = p.number_to_words(minutes, andword = "")
    return words

if __name__ == "__main__":
    main()
