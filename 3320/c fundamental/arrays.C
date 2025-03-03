#include <stdio.h>

int main() {int myNumbers[] = {25, 50, 75, 100};
int i;

for (i = 0; i < 4; i++) {
printf("%d\n", myNumbers[i]);
};

int myNums2[4];

myNums2[0] = 25;
myNums2[1] = 50;
myNums2[2] = 75;
myNums2[3] = 100;

for (i = 0; i < 4; i++) {
printf("%d\n", myNums2[i]);
};

int length = sizeof(myNums2) / sizeof(myNums2[0]);
printf("%d", length);

char greetings[] = "Hello World!"; // a string Array 
printf("%s", greetings);
printf("%c", greetings[0]);
greetings[2] = 'J';

char carName[] = "Volvo";

length = sizeof(carName) / sizeof(carName[0]);
for (i = 0; i < length; ++i) {
    printf("%c\n", carName[i]);
}
return 0;
}