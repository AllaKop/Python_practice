import time

seconds = time.time()
# For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins).
print("Seconds since epoch =", seconds)

print("This is printed immediately.")
time.sleep(2)
print("This is printed after 2 seconds.")

# time.struct_time Class
# Several functions in the time module such as
# gmtime(), asctime() etc. either take time.struct_time object as an argument or return it.

# The localtime() function takes
# the number of seconds passed since epoch as an argument and returns struct_time in local time.

result = time.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

# The gmtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in UTC.

result = time.gmtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

# The mktime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time)
# as an argument and returns the seconds passed since epoch in local time.

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

local_time = time.mktime(t)
print("Local time:", local_time)

# The asctime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time)
# as an argument and returns a string representing it.

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)

# The strftime() function takes struct_time (or tuple corresponding to it)
# as an argument and returns a string representing it based on the format code used.

named_tuple = time.localtime()  # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)

# Create a digital clock

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    time.sleep(1)
    
