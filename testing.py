import dayDifference
from datetime import date

current = date.strftime(date.today(), "%d-%m-%Y")


# Driver program
dt1 = dayDifference.Date("16-11-2022")
dt2 = dayDifference.Date(current)

print(dayDifference.numberOfDays(dt1, dt2), "days")
