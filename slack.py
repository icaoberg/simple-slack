#!/usr/bin/python3

import os.path
import os
import datetime
from tabulate import tabulate
from argparse import ArgumentParser
import warnings
from warnings import warn as warning

parser = ArgumentParser()
parser.add_argument( '-u', '--username', dest='username', default=None, help='Username to message' )
parser.add_argument( '-m', '--message', dest='message', default=None, help='Message')
parser.add_argument( '-c', '--channel', dest='channel', default=None, help='Channel to message')
results = parser.parse_args()

# read secrets. assumes file exists in ~/.SLACK_SECRETS
from pathlib import Path
file = str(Path.home()) + os.sep + '.SLACK_SECRETS'
exec(open(file).read())

if results.username != None and results.channel == None:
	direct_message = True
	message_channel = False
elif results.username == None and results.channel != None:
	direct_message = False
	message_channel = True
else:
	direct_message = True
	message_channel = True

if direct_message:
	if results.username == 'bsanchez':
		url = DIRECT_MESSAGE_BSANCHEZ
	elif results.username == 'icaoberg':
		url = DIRECT_MESSAGE_ICAOBERG
	else:
		print('Unknown username. Exiting method.')
		exit()

	command = 'curl -X POST -H \'Content-type: application/json\' --data \'{"text":"' + results.message + '"}\' ' + url
	os.system(command)
	exit()

if message_channel:
	if results.channel == 'general':
		url = CHANNEL_GENERAL
	elif results.channel == 'events':
		url = CHANNEL_EVENTS
	elif results.channel == 'programming':
		url = CHANNEL_PROGRAMMING
	elif results.channel == 'random':
		url = CHANNEL_RANDOM
	else:
		print('Unknown channel name. Exiting method.')
		exit()

	command = 'curl -X POST -H \'Content-type: application/json\' --data \'{"text":"' + results.message + '"}\' ' + url
	os.system(command)
	exit()
