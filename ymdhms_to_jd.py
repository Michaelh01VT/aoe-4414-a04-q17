# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
# Converts a given date and time (year, month, day, hour, minute, second) to fractional Julian date.
#
# Parameters:
# year: Integer
# month: Integer 1-12
# day: Integer 1-31
# hour: Integer 0-23
# minute: Integer 0-59
# second: Decimal
#
# Output:
# jd_frac: The fractional Julian Date 
#
# Written by Michael Hoffman
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys  # argv
import math  # math module

# Helper functions
def ymdhms_to_jd(year, month, day, hour, minute, second):
    # If month is January or February treat  as month 13 or 14 of previous year
    if month <= 2:
        year -= 1
        month += 12

    # Calculate the Julian date
    A = math.floor(year / 100)
    B = 2 - A + math.floor(A / 4)
    C = math.floor(365.25 * (year + 4716))
    D = math.floor(30.6001 * (month + 1))
    
    jd = C + D + day + B - 1524.5
    day_fraction = (hour + minute / 60 + second / 3600) / 24
    jd_frac = jd + day_fraction

    return jd_frac

# Initialize script arguments
year = 0
month = 0
day = 0
hour = 0
minute = 0
second = 0.0

# Parse script arguments
if len(sys.argv) == 7:
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
    hour = int(sys.argv[4])
    minute = int(sys.argv[5])
    second = float(sys.argv[6])
else:
    print('Usage: python3 ymdhms_to_jd.py year month day hour minute second')
    exit()

# Conversion to fractional Julian Date
jd_frac = ymdhms_to_jd(year, month, day, hour, minute, second)

# Print fractional Julian Date
print(jd_frac)
