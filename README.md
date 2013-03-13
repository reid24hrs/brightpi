brightpi
========

The Raspberry Pi Python Brightness Sensor runs on a Raspberry Pi. It takes a picture from a USB webcam and works out the brightness using the Python Imaging Library http://www.pythonware.com/products/pil/.

Once this is done the program then tries to upload the date+time and brightness to a line in a Google Drive Spreadsheet.

You will need to ensure that gspread is installed on your Raspberry Pi https://github.com/burnash/gspread.git

You can clone this code from your Raspberry Pi using git clone http://github.com/reid24hrs/brightpi.

You will also need a Google Drive account. Create a spreadsheet in you Google Drive called brightness.gsheet. Create a column called 'Date/Time' and column called 'Brightness'. You should also delete the 99 empty rows.
