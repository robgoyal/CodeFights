/* Name: studentsMarksSum.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Return the sum of students with provided parameter, gender
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int marks_summation(int* marks, int number_of_students, char gender) {
  //Write your code here.

    int start = 0, sum = 0;
    if (gender == 'g') {
        start = 1;
    }

    for (; start < number_of_students; start+=2) {
        sum = sum + *(marks + start);
    }

    return sum;
}

int main() {
    int number_of_students;
    char gender;
    int sum;

    scanf("%d", &number_of_students);
    int *marks = (int *) malloc(number_of_students * sizeof (int));

    for (int student = 0; student < number_of_students; student++) {
        scanf("%d", (marks + student));
    }

    scanf(" %c", &gender);
    sum = marks_summation(marks, number_of_students, gender);
    printf("%d", sum);
    free(marks);

    return 0;
}
