#include <stdio.h>

unsigned char limit = 150;
int counter;

int main() {
    for (unsigned char i=0; i < limit * 2; ++i) {
        printf("The loop executed %d times", i);
    }
}