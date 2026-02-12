import datetime

date = datetime.date(2026, 1, 13)
today = datetime.date.today()

time = datetime.time(12,30,0)
real_time = datetime.datetime.now()

real_time = real_time.strftime("%H:%M:%S %d.%m.%Y")

target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed.")
else:
    print("Target date has not passed.")


