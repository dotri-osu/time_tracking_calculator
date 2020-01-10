# Date: 11/04/19
# Calculate the first half of the day.
# Intended to use when start time is different than expected start time.

import math

class Timeblock:

    def __init__(self, hr, mins):
        self.hr = hr
        self.mins = mins

def morning_timeblock(this_week, checkin, est_checkout):
    ''' Takes in check-in time for the beginning of the day and projects how much time has been earned.'''

    # Calculate time earned
    morning_hrs = est_checkout.hr - checkin.hr
    print('morning hours: ' + str(morning_hrs))
    
    if est_checkout.mins == 0:
        morning_mins = 60 - checkin.mins
        print('checkin mins: ' + str(morning_mins))
        morning_mins = morning_mins / 60
        print('morning mins: ' + str(morning_mins))
        
    elif est_checkout.mins > 0 and est_checkout.mins < checkin.mins:
        morning_mins = 60 - checkin.mins
        print('checkin mins: ' + str(morning_mins))
        morning_mins = morning_mins / 60
        print('morning mins: ' + str(morning_mins))
        
    else:
        morning_mins = est_checkout.mins - checkin.mins
        print('checkin mins: ' + str(morning_mins))
        morning_mins = morning_mins / 60
        print('morning mins: ' + str(morning_mins))
        
    morning_total = morning_hrs + morning_mins

    
    this_week_new = this_week + morning_total

    # Display the remaining hours required to complete 40hr work week.
    if this_week_new > 32:
        print('This Week:' + str(this_week_new))
        # Calculate the amount of time needed to reach 40 hours
        rem_time = 40 - this_week_new    # Float of total hours remaining to meet weekly 40 hours.
        print(rem_time)
        rem_hrs = rem_time // 1                 # Total hours worked.
        rem_mins = rem_time - rem_hrs           # Total percentage of hour remaining.
        rem_mins *= 60                          # Converts percentage of hour to minutes.
        print(math.ceil(rem_hrs), 'hrs', math.ceil(rem_mins),'mins to complete 40 hr work week.')

            
this_week = float(input("Enter the total hours worked This Week: "))
morning_checkin_hr = int(input("Enter the hour of check-in: "))
morning_checkin_min = int(input("Enter the minute of check-in (format: 00): "))
lunch_checkout_hr = int(input("Enter the hour of check-out for lunch: "))
lunch_checkout_min = int(input("Enter the minute of check-out for lunch: " ))
this_week_new = ''

checkin = Timeblock(morning_checkin_hr, morning_checkin_min)
est_checkout = Timeblock(lunch_checkout_hr, lunch_checkout_min)
print(morning_timeblock(this_week, checkin, est_checkout))
##print(checkout_time(this_week))
