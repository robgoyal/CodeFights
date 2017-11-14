# Name: gradingStudents.py
# Author: Robin Goyal
# Last-Modified: November 10, 2017
# Purpose: Round a students grade from a set of criteria

def gradingStudents(grades):
    '''
    grades: list of grades to round if required

    output: list of rounded grades
    '''

    rounded_grades = []

    for grade in grades:

        # Calculate the difference to the closest multiple to 5
        multiple_to_5 = (5 - grade % 5)

        # Check if grade less than 38 or difference is too large
        if (grade < 38 or multiple_to_5 > 2):
            rounded_grades.append(grade)
        else:
            rounded_grades.append(grade + value_to_5)

    return rounded_grades