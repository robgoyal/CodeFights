# Name: boxBlur.py
# Author: Robin Goyal
# Last-Modified: July 11, 2017
# Purpose: Compress the matrix of pixels by creating a new image where
#          the average of each set of 3x3 pixels is taken
# Note: This algorithm could be done in one line but it would be longer
#       than it already is

def boxBlur(image):
    
    newImage = []
    for i in range(len(image) - 2):
        
        # Append each row of new image
        newImage.append([matrixSum([image[i][j:j+3], image[i+1][j:j+3],\
            image[i+2][j:j+3]]) for j in range(len(image[0]) - 2)])
        
    return newImage 

# Calculate the average of a 3x3 pixel
def matrixSum(array):
    temp = sum(map(sum, array))
    return temp // 9