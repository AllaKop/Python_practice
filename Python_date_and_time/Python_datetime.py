import datetime as dt
import pytz

print(dt.date.today())

time1 = dt.time(10, 45, 30, 45667)
print(time1)

print('Hours:', time1.hour)

current_datetime = dt.datetime.now()
print(current_datetime)

next_new_year = dt.datetime(2023, 1, 1)

time_remaining = next_new_year - current_datetime
print(time_remaining)

string_date = current_datetime.strftime("%A, %B, %d, %Y")
print(string_date)

date_string = "21 June, 2021"
date_object = dt.datetime.strptime(date_string, "%d %B, %Y")
print("Data object:", date_object)

print(dir(dt))

# Timezone handling

local = dt.datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = dt.datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = dt.datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

tz_Kyiv = pytz.timezone('Europe/Kyiv')
datetime_Kyiv = dt.datetime.now(tz_Kyiv)
print("Kyiv:", datetime_Kyiv.strftime("%m/%d/%Y, %H:%M:%S"))
