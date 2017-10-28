# Name: bonAppetit.py
# Author: Robin Goyal
# Last-Modified: October 27, 2017
# Purpose: Determine if the bill was split evenly based off of foods eaten
#          by each person

def bonAppetit(size, ignored_dish, bill, dishes):

    # Calculate exact value of split bill
    actual_split_bill = int(sum(dishes - dishes[ignored_dish]) / 2)

    # Print bon appetit if bill is evenly split, otherwise return difference
    if actual_split_bill == bill:
        return "Bon Appetit"
    else:
        return bill - actual_split_bill