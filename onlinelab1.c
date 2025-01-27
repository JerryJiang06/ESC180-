#include <ctype.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int linear_search(int *a, int sz, int elem) {
    for (int i=0; i<sz; i++) {
        if (*(a+i)==elem) {
            return i;
        }
    }
}

void reverse_arr(int *arr, int sz) {
    for (int i=0; i<sz/2; i++) {
        int k = arr[i];
        arr[i] = arr[sz-1-i];
        arr[sz-1-i] = k;
    }
}

int main() {
    
    
    return 0;
}