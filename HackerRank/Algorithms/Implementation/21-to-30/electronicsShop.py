# Name: electronicsShop.py
# Author: Robin Goyal
# Last-Modified: November 21, 2017
# Purpose: Calculate the amount of money spent at an electronics shop


def getMoneySpent(keyboards, drives, s):
    '''
    The maximum amount of money that can be spent on a single keyboard
    and drive without exceeding her budget

    s: max budget
    keyboards: list of prices for keyboards
    drives: list of prices for drives

    return: int represent money spent, -1 if no money spent
    '''

    # Initialize max
    max_combo_price = -1

    for keyboard in keyboards:

        # View current maximum combo price for 1 keyboard and match with all drives
        curr_max_combo_price = -1
        for drive in drives:
            combo_price = keyboard + drive

            # Check if combo is greater than the current max and if less than budget
            if combo_price > curr_max_combo_price and combo_price < s:
                current_max = combo_price

        # Update the maximum combo price
        if current_max > max_combo_price:
            max_combo_price = curr_max_combo_price

    return max_combo_price


def main():

    # Retrieve problem inputs
    s, n, m = list(map(int, input().strip().split(' ')))
    keyboards = list(map(int, input().strip().split(' ')))
    drives = list(map(int, input().strip().split(' ')))

    #  Max amount of money she can spend on a keyboard and drive
    # -1 if she can't purchase both items
    moneySpent = getMoneySpent(keyboards, drives, s)
    print(moneySpent)
