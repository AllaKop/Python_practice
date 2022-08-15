import threading
import time


def print_hello_three_times():
    for i in range(3):
        print("Hello")


def print_hi_three_times():
    for i in range(3):
        print("Hi")


t1 = threading.Thread(target=print_hello_three_times)
t2 = threading.Thread(target=print_hi_three_times)

t1.start()
t2.start()


# The sleep() function suspends execution of the current thread for a given number of seconds.

def print_hello():
    for i in range(4):
        time.sleep(0.5)
        print("Good Morning")


def print_hi():
    for i in range(4):
        time.sleep(0.6)
        print("Good Evening")


t1 = threading.Thread(target=print_hello)
t2 = threading.Thread(target=print_hi)
t1.start()
t2.start()
