# Name: growingPlant.py
# Author: Robin Goyal
# Last-Modified: July 20, 2017
# Purpose: Determine the number of days required for a plant to reach a desired
#          height with a specified growth speed from the sun and ungrowth 
#          speed at night

def growingPlant(upSpeed, downSpeed, desiredHeight):

    # Return 1 day if the desired height is less than growht speed
    if desiredHeight < upSpeed:
        return 1

    return int(float(desiredHeight) / (upSpeed - downSpeed))