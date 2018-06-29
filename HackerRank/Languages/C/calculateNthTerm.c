/* Name: calculateNthTerm.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Output nth term of series
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int find_nth_term(int n, int a, int b, int c) {
  //Write your code here.
    if (n == 1) {
        return a;
    }
    else if (n == 2) {
        return b;
    }
    else if (n == 3) {
        return c;
    }

    return find_nth_term(n-1, a, b, c);
}

int main() {
    int n, a, b, c;

    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);

    printf("%d", ans);
    return 0;
}
