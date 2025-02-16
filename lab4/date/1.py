import datetime

x = datetime.datetime.now()
day5 = int(x.strftime("%d"))
print(f"Year {x.year}, month {x.month},", "day", day5-5)