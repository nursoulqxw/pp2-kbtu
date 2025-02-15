from datetime import date
today=date.today()
christmas = date(date.today().year, 12, 25)
until_christmas = christmas - today
print(until_christmas)