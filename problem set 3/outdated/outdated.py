months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("date: ").strip()
    try:
        if '/' in date:
            month, day, year = date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
        else:
            month_name, day, year = date.split(" ")
            if not day.endswith(','):
                continue
            day = int(day.rstrip(','))
            month = months.index(month_name) + 1
            year = int(year)

        if not (1 <= day <= 31 and 1 <= month <= 12):
            continue

        print(f"{year}-{month:02}-{day:02}")
        break

    except ValueError:
        pass
