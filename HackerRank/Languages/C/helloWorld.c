/* Name: helloWorld.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Print formatted string Hello World
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    char s[100];
    scanf("%[^\n]%*c", &s);

    printf("Hello, World!\n");
    printf("%s", s);
    return 0;
}
