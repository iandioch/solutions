from datetime import date

days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
]
day, month = [int(s) for s in input().split()]
date = date(2009, month, day)
print(days[date.weekday()])
