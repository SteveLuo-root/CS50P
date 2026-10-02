import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        students = []
        for row in reader:
            last, first = row["name"].split(", ")
            students.append({"first": first, "last": last, "house": row["house"]})

    with open(sys.argv[2], "w") as file:
        write = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        write.writeheader()
        for student in students:
            write.writerow(student)

except FileNotFoundError:
    sys.exit(f"Counld not read {sys.argv[1]}")
