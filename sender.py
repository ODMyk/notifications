from datetime import datetime
from time import sleep
import plyer
import json
import sys
from os import path as p

if p.isdir(sys.argv[0]):
	path = sys.argv[0]
else:
	path = sys.argv[0]+'\\..'



with open("".join((path, '\\temp.json')), "r") as j:
	time, msg, title = json.load(j)

icon = "".join((path, '\\bell.ico'))

# waiting for time hours:minutes:00
while datetime.now().second != 0:
	sleep(1)
	x = datetime.now()

h = time[0] - x.hour # calculating time to wait before sending notification 
m = time[1] - x.minute
if m < 0:
	h -= 1
	m = 60 + m 

seconds_to_sleep = m*60 + h*3600 # there are 60 seconds in 1 minute and 3600 seconds in 1 hour

if seconds_to_sleep > 0:
	sleep(seconds_to_sleep)

plyer.notification.notify( # sending a notification with simple function
	message = msg,
	app_name = 'Notifications',
    app_icon = icon,
    title = title )
