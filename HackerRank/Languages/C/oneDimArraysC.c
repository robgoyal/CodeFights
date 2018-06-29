/* Name: oneDimArraysC.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Print the sum of the integers of an array
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);

    int *arr = (int *) malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        scanf("%d", (arr + i));
    }

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += *(arr + i);
    }

    printf("%d", sum);

    return 0;
}
