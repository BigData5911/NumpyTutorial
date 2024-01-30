
from datetime import date, datetime, time

my_date = date(1999,9,9)

my_datetime = datetime.fromtimestamp(1500000000)

print(my_date, date.today(), time.isoformat(my_datetime.time()))