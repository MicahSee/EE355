/*
    The code to collect the input is based on this post from Stack Overflow: 
    https://stackoverflow.com/questions/2539796/c-reading-multiple-numbers-from-single-input-line-scanf
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int size;
    int *int_array;
    int *sum_array;

    printf("Size of the input array: ");
    scanf("%d", &size);
    
    int_array = malloc(size * sizeof(int));
    sum_array = malloc(size * sizeof(int));

    printf("Enter array items (one per line):\n");
    for (int i=0; i < size; i++) {
        scanf("%d", &int_array[i]);
    }

    for (int i=0; i < size; i++) {
        int prod = 1;

        for (int j=0; j < size; j++) {
            if (j != i) {
                prod = prod * int_array[j];
            }
        }

        sum_array[i] = prod;
    }

    printf("New array:");

    for (int i=0; i < size; i++) {
        printf(" %d", sum_array[i]);
    }

    printf("\n");

    free(int_array);
    free(sum_array);

    return 0;
}