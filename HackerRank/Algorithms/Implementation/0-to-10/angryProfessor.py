# Name: angryProfessor.py
# Author: Robin Goyal
# Last-Modified: October 24, 2017
# Purpose: Print the status of the class:
#               - Yes if there are not "min_student" number of students in class
#               - No if there are at least "min_student" number of students in class

def angryProfessor(min_students, students):

    # Calculate the number of students in class
    num_students_in_class = sum(list(map(lambda x: x <= 0, students)))

    if num_students_in_class >= min_students:
        print("NO")
    else:
        print("YES")