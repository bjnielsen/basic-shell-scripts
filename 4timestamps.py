#!/usr/bin/python

import sys
import re
import os
import time
import datetime


logfilepath = '/home/bryan/tmp/'
current_date = str(datetime.date.today())
epochtime = str(time.time())
# 3  	tm_hour  	range [0,23], 4  	tm_min  	range [0,59],   5  	tm_sec  	range [0,61]; 
# i.e. (2008, 6, 17, 11, 35, 13, 1, 169, 1)  where hr=11, min=35, sec=13
current_hr = str("%02d" % time.localtime()[3])
current_min = str("%02d" % time.localtime()[4])
current_sec = str("%02d" % time.localtime()[5])
current_time = current_hr + ":" + current_min + ":" + current_sec
logfilename = logfilepath + current_date + "-" + current_time

print current_hr
print current_min
print current_sec
print current_time
print logfilename
print "Epoch time is: " + epochtime

# Time in Min:Sec
time = str("%02d" % time.localtime()[3]) + ":" + str("%02d" % time.localtime()[4])
print time
