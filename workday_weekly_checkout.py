# Date: 11/04/19
# Program to return when to check out based on 40 hour work week.
# Program assumes M-Th time blocks are populated correctly.
# And 1st time block on Friday is closed. Takes in a start time after lunch and projects time to check out.
# Last updated: 12/31/19 - Calculation of remaining time was off and producing negative numbers.

import math

class Checkout_time:
    ''' Initialize the total hours worked, and the hour and minute of last check in.'''

    def __init__(self, weekly_total, hr, mins):
        self.weekly_total = weekly_total
        self.hr = hr
        self.mins = mins

def friday_checkout(checkin):
    ''' Takes in check-in time for last time block and returns check-out time.'''

    add_hrs = 0

    # Calculate the amount of time needed to reach 40 hours
    rem_time = 40 - checkin.weekly_total    # Float of total hours remaining to meet weekly 40 hours.
    rem_hrs = rem_time // 1                 # Total hours worked.
    rem_mins = rem_time - rem_hrs           # Total percentage of hour remaining.
    rem_mins *= 60                          # Converts percentage of hour to minutes.
    
    print(math.ceil(rem_hrs), 'hrs', math.ceil(rem_mins),'mins to complete 40 hr work week.')

    # Calculate minutes    
    checkin.mins += rem_mins
    
    if checkin.mins >= 60:
        add_hrs = checkin.mins // 60
        minus_mins = add_hrs * 60
        checkin.mins -= minus_mins

    # Calculate hours
    checkin.hr += rem_hrs + add_hrs

    if checkin.hr > 12:
        checkin.hr -= 12

    # Return Check-out Time
    if checkin.mins == 0:
        print('Checkout at: ', int(checkin.hr),'pm')
    else:
        print('Checkout at: ', int(checkin.hr),':', math.ceil(checkin.mins), 'pm')


# test case
weekly_total = float(input('Enter this weeks total worked hours: '))

if weekly_total >= 40:
    print('What are you doing here? Go home!')
    
else:
    enter_hr = int(input('Enter the hour of check-in: '))
    enter_min = int(input('Enter the minute of check-in: '))

    checkin = Checkout_time(weekly_total,enter_hr,enter_min)
    print(friday_checkout(checkin))

input(print('press enter to exit'))
