def power(a, b, n):
    return pow(a, b, n)

n = int(input("Enter prime number (n): "))
g = int(input("Enter primitive root (g): "))

x = int(input("Private key of Person 1: "))
y = int(input("Private key of Person 2: "))

A = power(g, x, n)
B = power(g, y, n)

key1 = power(B, x, n)
key2 = power(A, y, n)

print("Key for Person 1:", key1)
print("Key for Person 2:", key2)

if key1 == key2:
    print("Key exchange successful!")
else:
    print("Key exchange failed.")
