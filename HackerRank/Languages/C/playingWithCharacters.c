/* Name: playingWithCharacters.c
   Author: Robin Goyal
   Last-Modified: June 28, 2018
   Purpose Print a character, word, and sentence
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char ch;
    char s[100];
    char sen[100];


    scanf("%c", &ch);
    scanf("%s", s);
    scanf("\n");

    scanf("%[^\n]%*c", sen);

    printf("%c\n%s\n%s", ch, s, sen);
    return 0;
}
