# from datetime import date
from datetime import date


current = date.strftime(date.today(), "%d-%m-%Y")
current1 = date.strftime(date.today(), "%d-%m-%Y")

d1 = date.strptime(current, "%Y/%m/%d")
d2 = date.strptime(current1, "%Y/%m/%d")
difference = d1-d2
print(difference.days)

# from datetime import date

# a = date.today()
# b = (date(2022, 11, 14)).strftime('%d-%m-%Y')
# # b.strftime('%d-%m-%Y')
# print(a)
# print(b)


# print((b-a).days)

# from datetime import datetime

# # dates in string format
# str_d1 = '2021/10/20'
# str_d2 = '2022/2/20'

# # convert string to date object
# d1 = datetime.strptime(str_d1, "%Y/%m/%d")
# d2 = datetime.strptime(str_d2, "%Y/%m/%d")

# # difference between dates in timedelta
# delta = d2 - d1
# print(f'Difference is {delta.days} days')
