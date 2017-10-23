# Name: plusMinus.py
# Author: Robin Goyal
# Last-Modified: October 22, 2017
# Purpose: Print the fraction of positive, negative and zero numbers 
#          in the array

def plusMinus(size, arr):

    # Calculate number of positive, negative, and zero values
    num_pos_values = len(list(filter((lambda x: x > 0), arr)))
    num_neg_values = len(list(filter((lambda x: x < 0), arr)))
    num_zeo_values = len(list(filter((lambda x: x == 0), arr)))

    print("{}\n{}\n{}".format(num_pos_values/n, num_neg_values/n, num_zeo_values/n))