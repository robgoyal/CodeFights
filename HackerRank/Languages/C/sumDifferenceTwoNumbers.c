/* Name: sumDifferenceTwoNumbers.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Print the sum and difference of two numbers
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    // Initialize variables
    int x, y;
    float a, b;

    scanf("%d %d", &x, &y);
    scanf("%f %f", &a, &b);

    printf("%d %d\n", x + y, x - y);
    printf("%.1f %.1f\n", a + b, a - b);

    return 0;
}
