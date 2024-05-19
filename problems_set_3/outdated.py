date=[
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
def main():
    for i in date:
        print(i)
    c =input("date:")
    print (pattern(c))

def pattern(d):
    if d in date:
        month = date[d]
        formatted_date = f"{year:04d}-{month:02d}-{int(day):02d}"
        f"{formatted_date}")
        return d


main()
