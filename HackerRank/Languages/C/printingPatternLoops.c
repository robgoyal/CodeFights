/* Name: printingPatternLoops.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Print a pattern containing numbers from 1 to n
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int max(int a, int b);

int main()
{

    int n;
    int tmp;
    scanf("%d", &n);

    // 2n+1 by 2n+1 grid
    for (int i = (-n + 1); i < n; i++) {
        for (int j = (-n + 1); j < n; j++) {
            tmp = max(i, j);
            printf("%d ", tmp + 1);
        }
        printf("\n");
    }

    return 0;
}


int max(int a, int b) {
    if (abs(a) > abs(b)) {
        return abs(a);
    }

    return abs(b);
}
