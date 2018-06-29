/* Name: sumDigitsFiveDigitNumber.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Print the sum of digits of a number
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n;
    scanf("%d", &n);

    int sum;
    while (n != 0) {
        sum += (n % 10);
        n /= 10;
    }

    printf("%d", sum);
    return 0;
}
