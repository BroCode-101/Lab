#include <stdio.h>
#include <math.h>

void calculateParityBits(int data[], int n) {
    int r = 0, m = n;
    while ((m + r + 1) > pow(2, r)) {
        r++;
    }
    int hammingCode[m + r + 1];
    int j = 0, k = 0;
    for (int i = 1; i <= m + r; i++) {
        if ((i & (i - 1)) == 0) {
            hammingCode[i] = 0;
        } else {
            hammingCode[i] = data[j++];
        }
    }
    for (int i = 1; i <= m + r; i++) {
        if ((i & (i - 1)) == 0) {
            int parity = 0;
            for (int k = i; k <= m + r; k++) {
                if ((k & i) == i) {
                    parity ^= hammingCode[k];
                }
            }
            hammingCode[i] = parity;
        }
    }
    printf("Encoded Hamming Code: ");
    for (int i = 1; i <= m + r; i++) {
        printf("%d", hammingCode[i]);
    }
    printf("\n");
}

int main() {
    int n;
    printf("Enter the number of data bits: ");
    scanf("%d", &n);
    int data[n];
    
    for (int i = 0; i < n; i++) {
        printf("Enter the data bits: ");
        scanf("%d", &data[i]);
    }
    calculateParityBits(data, n);
    return 0;
}