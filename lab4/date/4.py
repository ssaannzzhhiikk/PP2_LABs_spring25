from datetime import datetime

dt1 = datetime(2024, 2, 10, 12, 0, 0)
dt2 = datetime(2024, 2, 11, 14, 30, 0)

diff_seconds = (dt2 - dt1).total_seconds()

print("Difference in seconds:", diff_seconds)