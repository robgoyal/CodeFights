/* Name: functionsInC.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Print the greatest of four integers
*/

#include <stdio.h>

int max_of_four(int a, int b, int c, int d);

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}

int max_of_four(int a, int b, int c, int d) {
    int arr[] = {a, b, c, d};

    int max = arr[0];

    for (int i = 0; i < 4; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    return max;
}
