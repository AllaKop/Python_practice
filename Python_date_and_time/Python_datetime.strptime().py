# The strptime() method creates a datetime object from the given string.
# You cannot create datetime object from every string. The string needs to be in a certain format.

import datetime

date_string = "21 June, 2018"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
print("type of date_object =", type(date_object))

# If the string (first argument) and the format code (second argument) passed to the strptime()
# doesn't match, you will get ValueError.

date_string = "12/11/2018"
date_object = datetime.datetime.strptime(date_string, "%d %m %Y")

print("date_object =", date_object)