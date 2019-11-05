from datetime import date, timedelta, datetime

now = datetime.strptime(input(), "%Y %m %d")
now += timedelta(int(input()))
print(str(now)[:10].replace('-0', ' ').replace('-', ' '))
