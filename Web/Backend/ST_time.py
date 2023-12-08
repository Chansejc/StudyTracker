import sqlite3 as sql
# Changing the strings from the time series into usable data
# Day of Week to numeric
dow_to_num = {
    'Mon': 1,
    'Tue': 2,
    'Wed': 3,
    'Thu': 4,
    'Fri': 5,
    'Sat': 6,
    'Sun': 7
}
# Month to Numeric
mth_to_num = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}
# ^ Changing the strings from the time series into usable data ^
time_dict = {
    "DoW": '',
    "Mnth": '',
    "DoM": '',
    "Time": '',
    "Year": ''
}


def get_maxtime_iter(time):
    new = time.split(" ")
    new.remove('')
    i = 0
    for item in time_dict:
        time_dict[item] = new[i]
        i += 1
    time_separated = time_dict["Time"].split(":")
    time_list = [int(i) for i in time_separated]
    time_number = 0  # Flag for time as a single integer
    hours_to_sec = 60 * (time_list[0] * 60)
    min_to_sec = 60 * time_list[1]
    sec = time_list[2]
    time_number += hours_to_sec + min_to_sec + sec
    print(time_list)
    return time_number


def get_stime_iter(time):
    time = time.split(":")
    time_list = [int(i) for i in time]
    time_number = 0  # Flag for time as a single integer
    hours_to_sec = 60 * (time_list[0] * 60)
    min_to_sec = 60 * time_list[1]
    sec = time_list[2]
    time_number += hours_to_sec + min_to_sec + sec
    return time_number

# Changing the CTime output into one iterable integer
# Using this integer to calculate time spent in a single session
# sesh_length.value = "X hour(s) and Y minute(s)"
# Set this equal to a variable to display the correct time signatures
def sesh_length(start, end):
    import math
    elapsed_time = end - start
    #print(elapsed_time)
    total_seconds = (elapsed_time % 60)
    total_minutes = math.floor((elapsed_time - total_seconds) / 60)
    total_minutes = total_minutes % 60
    total_hours = math.floor(elapsed_time / 3600)
    if elapsed_time < 0:
        total_hours = 24 + total_hours

    return {'Hours': total_hours, 'Minutes': total_minutes, 'Seconds': total_seconds}

'''
If hours : Session length = X hour(s) and Y minutes
Else : Session Length = Y minutes
'''
