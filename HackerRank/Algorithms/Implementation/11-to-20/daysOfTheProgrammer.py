# Name: daysOfTheProgrammer.py
# Author: Robin Goyal
# Last-Modified: November 13, 2017
# Purpose: Calculate the 256th day of the year in Russia

def main():

    year = int(input().strip())
    result = solve(year)
    print(result)

def solve(year):
    '''
    year: year between 1700 and 2700

    return: the date in dd.mm.yyyy format displaying the 256th day
    '''

    # Julian leap year only required the year to be divisible by 4
    is_gregorian_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 == 0)
    is_julian_leap = (year % 4 == 0)

    # The 256th day always fell in September (9th month)
    month = 9

    # 1918 had 14 days in February
    if year == 1918:
        day = 26
    elif (year < 1918 and is_julian_leap) or (is_gregorian_leap):
        day = 12
    else:
        day = 13

    return '{}.0{}.{}'.format(day, month, year)

if __name__=="__main__":
    main()