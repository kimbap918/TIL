import datetime
start_date = datetime.date(2014, 4, 2)
n = int(input())
celebration_date = start_date + datetime.timedelta(days=n-1)
print(celebration_date.strftime("%Y-%m-%d"))