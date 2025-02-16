import datetime

x = datetime.datetime.now()

no_micro = x.replace(microsecond=0)
print(no_micro)