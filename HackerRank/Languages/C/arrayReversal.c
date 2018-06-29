/* Name: arrayReversal.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Return an array of size n
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }

    for (int tmp, i = 0; i < (num / 2); i++) {
        tmp = *(arr + i);
        *(arr + i) = *(arr + (num - i - 1));
        *(arr + (num - i - 1)) = tmp;
    }

    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}
