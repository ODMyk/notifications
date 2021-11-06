from os import system
import json
import sys
from os import path as p

if p.isdir(sys.argv[0]):
	path = sys.argv[0]
else:
	path = sys.argv[0] + '\\..'

h, m = None, None
while h is None or m is None:
	try:
		print('\nWrite time when notification will be sent. Example: 17 45')
		h, m = (int(x) for x in input('Time: ').split())
		if h > 23 or m > 59:
			print('Incorrect input!')
			h, m = None, None
	except:
		print('Incorrect input!')
		h, m = '0', '0'
time = (h, m)

print('\nOK. Now write title of your notification.')
title = input('Title: ')

print('\nOK. Now write message of your notification.')
msg = input('Message: ')

args = [time, msg, title]

with open("".join((path, '\\temp.json')), 'w') as j:
    json.dump(args, j)

system("".join(('wscript.exe ', path, '\\Invisible.vbs ', path, '\\starter.bat')))

sys.exit()
