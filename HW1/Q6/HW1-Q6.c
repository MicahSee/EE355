#include <stdio.h>

int main() {
    int x, y;

    x = 10;
    y = 15;

    printf("Values before swap:\nx=%d, y=%d\n", x, y);

    x = x + y;
    y = x - y;
    x = x - y;

    printf("Values after swap:\nx=%d, y=%d\n", x, y);
}