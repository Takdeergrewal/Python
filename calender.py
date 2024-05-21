# This program is built by Krimy Tarpara. 
# It asks the user for a year between 1970 to 2030 and displays the calender. 
# I finished this on 22-07-2023.

# For the leap year
def isLeap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# For the first day of the year
def firstFunction(year):
    offset = 4
    for y in range(1970, year):
        if isLeap(y):
            offset += 366
        else:
            offset += 365
    return offset % 7

def monthFunction(month, offsetYear, year):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(year):
        monthDays[1] = 29
    offset = offsetYear
    for x in range(month - 1):
        offset += monthDays[x]
    return offset % 7

# For the months and days of the year
def yearFunction(month, offsetMonth, monthDays):
    print("Sun Mon Tue Wed Thu Fri Sat")
    print("    " * offsetMonth, end="")
    for day in range(1, monthDays + 1):
        print(f"{day:2d} ", end=" ")
        if (day + offsetMonth) % 7 == 0:
            print()
    print()

# asking user for input and checking the range of the year
def data():
    while True:
        year = input("Enter 4-digit year to print the calender or 0 to quit:\n")
        print("          ", year)
        if year == "0":
            return int(year)
        if year.isdigit() and 1970 <= int(year) <= 2030: # Year range from 1970 to 2030
            return int(year)
        else:
            print("Sorry! Enter a valid year between 1970 and 2030 or 0 to quit.")

# printing the output 
def main():
    while True:
        year = data()
        if year == 0:
            break
        offsetYear = firstFunction(year)
        monthDays = [31, 28 + isLeap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        monthList = ["          January", "          February", "          March", "          April", \
                     "          May", "          June", "          July", "          August", \
                     "          September", "          October", "          November", "          December"]
        for month in range(1,13):
            print(f"\n{monthList[month-1]}")
            month_offset = monthFunction(month, offsetYear, year)
            yearFunction(month, month_offset, monthDays[month-1])

if __name__ == "__main__":
    main()
