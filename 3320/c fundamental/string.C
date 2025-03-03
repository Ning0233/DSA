#include <stdio.h>
#include <string.h>

int main()
{char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
printf("%d", strlen(alphabet));

char str1[20] = "Hello";
char str2[] = "World!";

strcat(str1, str2);

printf("%s", str1);

char str1[20] = "Hello World!";
str2[20];

strcpy(str1, str2);
printf("%s", str2);
printf("%d\n", strcmp(str1, str2));
}

