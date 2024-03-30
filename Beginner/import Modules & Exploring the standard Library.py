import sys
import random
import math
import datetime
import calendar
import os
import webbrowser

print(sys.path)


courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2018))

print(webbrowser.__file__)
webbrowser.open("http://xkcd.com/353/")