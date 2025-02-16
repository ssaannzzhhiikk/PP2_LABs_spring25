import datetime

x = datetime.datetime.now()

day = int(x.strftime("%d"))

print("Yesterday was:", day-1)
print("Today is:", day)
print("Tomorrow will be:", day+1)
