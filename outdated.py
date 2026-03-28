months = {
 "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}
while True:
    date = input('date: ').strip()

    try:
        #getting values for variables
        month, day, year = map(int, date.split('/'))
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break
    #acom for dif struc
    except (ValueError, AttributeError):
        try:
            #assings parts
            parts = date.split()
            month_name = parts[0].lower()
            day = int(parts[1].strip(","))
            year = int(parts[2])
            # get number from dic
            if month_name in months:
                month = months[month_name]
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
            #acom for invalid struc
        except (ValueError, IndexError):
            pass



import cowsay
