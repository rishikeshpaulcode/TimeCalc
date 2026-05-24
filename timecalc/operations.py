# Helper functions

# import required packages
from datetime import datetime
import random
import re

# global constants
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600

# function to validate given time (as string)
def is_valid(time_str):
    pattern = re.compile(r"^-?\d{1,2}:\d{2}:\d{2}$")
    if re.fullmatch(pattern, time_str):
        return True
    return False


# function to convert time_int into "HH:MM:SS" format
def format_time_int(time_int):
    sign = '-' if time_int < 0 else ''
    total_seconds = abs(time_int)

    hours = '0' + str(total_seconds // SECONDS_IN_HOUR)
    total_seconds %= SECONDS_IN_HOUR
    minutes = '0' + str(total_seconds // SECONDS_IN_MINUTE)
    total_seconds %= SECONDS_IN_MINUTE
    seconds = '0' + str(total_seconds)
    
    return f"{sign}{hours[-2:]}:{minutes[-2:]}:{seconds[-2:]}"


# function to parse time_str (calculate to number of seconds)
def parse_time_str(time_str):
    sign = 1
    if time_str.startswith('-'):
        sign = -1
        time_str = time_str[1:]

    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = sign * ((hours * SECONDS_IN_HOUR) + (minutes * SECONDS_IN_MINUTE) + seconds)
    return total_seconds


# function to get current time
def get_curr_time():
    curr_time = datetime.now()
    return f"{curr_time.hour}:{curr_time.minute}:{curr_time.second}"


# function to generate random timestamp
def gen_rand_time():
    hour = random.randint(0, 24)
    min = random.randint(0, 60)
    sec = random.randint(0, 60)
    return f"{hour}:{min}:{sec}"
