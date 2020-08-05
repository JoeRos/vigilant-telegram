# A practice program to get user's dob and calculate months, days and hours of life
# 07/20/20 - JMRosado
# Module information from geeksforgeeks.org

from datetime import datetime, timedelta, date
import calendar

# Delimiter to format user input
delim= '/'
# Load today's date
today = datetime.now()

birthdate = input('Enter your Date of Birth (mm/dd/yyyy): ')
# Error checking for invalid format
if delim in birthdate:
    dob=birthdate.split('/')
elif delim not in birthdate:
    print('Invalid Format please try again.')
    quit()
    
#Loading user entered date into a datetime object
birth= datetime(int(dob[2]), int(dob[0]), int(dob[1]),0,0,0)

#Calculating time passed since birth
delta= today-birth

# Calculate Months and days to display instead of a float value after number of years
yr_remain = delta.days%365.25
mo_remain = yr_remain/30.4375
dy_remain = yr_remain%30.4375

#Populating Month and year values from user input for calendar
yy = int(dob[2])
mm = int(dob[0])
# display the calendar
calendar.setfirstweekday(calendar.SUNDAY) 
print(calendar.month(yy, mm))
#Output
print('You have been alive:')
print(int(delta.days/365.25), 'Years', int(mo_remain), 'Months', dy_remain, 'Days')
print('or')
print(int(delta.days/30.4375), 'Months', dy_remain, 'Days' )
print('or')
print(delta.days, 'Days')
print('or')
print((delta.days*24), 'Hours')
print('or')
print(delta.days*1440, 'Minutes')
print('or')
print(delta.days*86400, 'Seconds')
