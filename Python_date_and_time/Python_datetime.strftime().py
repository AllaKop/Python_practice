import datetime

current_date = datetime.datetime.today()
print(current_date)

date1 = datetime.date(2021, 1, 5)
print(date1)

datetime_object = datetime.datetime(2021, 11, 28, 23, 44, 59)
print(datetime_object)
print(datetime_object.date())
print(datetime_object.time())

current_datetime = datetime.datetime.now()
print(current_datetime)

# The strftime() method returns a string representing date and time using date, time or datetime object.

date_time1 = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")
print(date_time1)
print(type(date_time1))

# Creating string from a timestamp

timestamp = 1528797322
date_time1 = datetime.datetime.fromtimestamp(timestamp)

print("Date time object:", date_time1)

d = date_time1.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)

d = date_time1.strftime("%d %b, %Y")
print("Output 3:", d)

d = date_time1.strftime("%d %B, %Y")
print("Output 4:", d)

d = date_time1.strftime("%I%p")
print("Output 5:", d)
