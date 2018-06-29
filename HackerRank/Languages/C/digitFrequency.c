/* Name: digitFrequency.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Find frequency of each digit in a string
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char *str = malloc(1001 * sizeof(char));
    scanf("%s", str);
    str = realloc(str, strlen(str) + 1);

    int *freq = (int *) calloc(10, sizeof(int));


    for (int i = 0; i < strlen(str); i++) {
        if (*(str + i) >= 48 && *(str + i) <= 57) {
            *(freq + (*(str+i) - 48)) += 1;
        }
    }

    for (int i = 0; i < 10; i++) {
        printf("%d ", *(freq + i));
    }

    free(str);
    free(freq);

    return 0;
}
