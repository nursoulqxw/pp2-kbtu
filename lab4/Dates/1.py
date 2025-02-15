from datetime import datetime

# x = datetime.datetime.now()

# print(x.day-5)

current_date = datetime.now()

new_date = datetime(current_date.year, current_date.month, current_date.day - 5)
print(new_date.strftime("%Y-%m-%d"))