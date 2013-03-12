#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime
import gspread
import Image
import ImageStat
import math
import os

# ===========================================================================
# Google Account Details
# ===========================================================================

# Account details for google docs
email       = 'you@somewhere.com'
password    = '$hhh!'
spreadsheet = 'SpreadsheetName'

# ===========================================================================
# Example Code
# ===========================================================================


# Login with your Google account
try:
  gc = gspread.login(email, password)
except:
  print "Unable to log in.  Check your email address/password"
  sys.exit()

# Open a worksheet from your spreadsheet using the filename
try:
  worksheet = gc.open(spreadsheet).sheet1
  # Alternatively, open a spreadsheet using the spreadsheet's key
  # worksheet = gc.open_by_key('0BmgG6nO_6dprdS1MN3d3MkdPa142WFRrdnRRUWl1UFE')
except:
  print "Unable to open the spreadsheet.  Check your filename: %s" % spreadsheet
  sys.exit()

# Continuously append data
while(True):
  # Run the webcam light brightness sensor program to get the brightness readings.

  os.system("fswebcam --no-banner --scale 50x50 -d /dev/video0 webcam.jpg")
  im = Image.open("webcam.jpg")
  stat = ImageStat.Stat(im)
  r,g,b = stat.mean
  brightness = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

  # Append the data in the spreadsheet, including a timestamp
  try:
    values = [datetime.datetime.now(), brightness]
    worksheet.append_row(values)
  except:
    print "Unable to append data.  Check your connection?"
    sys.exit()

  # Wait 30 seconds before continuing
  print "Wrote a row to %s" % spreadsheet
  time.sleep(30)
