/* Name: pointersInC.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Read two integers as arguments, set a as the sum and b as the difference
*/

#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
    // Complete this function
    int sum = *a + *b;
    int diff = abs(*a - *b);

    *a = sum;
    *b = diff;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
