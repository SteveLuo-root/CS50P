from tabulate import tabulate
import csv
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        rows = []
        for row in reader:
            rows.append(row)
        print(tabulate(rows[1:], headers = rows[0], tablefmt = "grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
