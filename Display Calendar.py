import calendar

year = int(input("Enter Year: "))
month = int(input("Enter month: "))
calendar = calendar.month(year, month)
print(calendar)
