import calendar
import datetime

cal = calendar.Calendar(firstweekday=0)

weeks = cal.monthdayscalendar(2026, 8)

for week in weeks:
    print(week)

print(datetime.date.today())  # noqa: DTZ011
date = datetime.date.today()  # noqa: DTZ011
year = date.year
print(year)
