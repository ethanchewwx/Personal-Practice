# import datetime
#
# days_each_year = {}
# for year in range(1901, 2001):
#     if year % 4 == 0:
#         days_each_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     else:
#         days_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     days_each_year[year] = days_each_month
# print(days_each_year)
#
# no_sundays = 0
# for year in range(1901, 2001):
#     for month in range(0, 12):
#         days_in_month = days_each_year[year][month]
#         for day in range(1, days_in_month + 1):
#             date = datetime.datetime(year=year, month=month + 1, day=day)
#             if date.weekday() == 6:
#                 no_sundays += 1


import datetime

months = [month for month in range(1, 13)]

no_sundays = 0
for year in range(1901, 2001):
    for month in months:
        date = datetime.datetime(year=year, month=month, day=1)
        if date.weekday() == 6:
            no_sundays += 1
print(no_sundays)