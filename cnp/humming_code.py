
def calculateParityBits(data, n):
    r = 0
    m = n
    while (m + r + 1) > 2**r:
        r += 1
    hammingCode = [0] * (m + r + 1)
    j = 0
    for i in range(1, m + r + 1):
        if (i & (i - 1)) == 0:
            hammingCode[i] = 0
        else:
            hammingCode[i] = data[j]
            j += 1
    for i in range(1, m + r + 1):
        if (i & (i - 1)) == 0:
            parity = 0
            for k in range(i, m + r + 1):
                if (k & i) == i:
                    parity ^= hammingCode[k]
            hammingCode[i] = parity
    print("Encoded Hamming Code: ", ''.join(map(str, hammingCode[1:])))

n = int(input("Enter the number of data bits: "))
data = [int(input(f"Enter the data bits {1+i}: ")) for i in range(n)]
calculateParityBits(data, n)