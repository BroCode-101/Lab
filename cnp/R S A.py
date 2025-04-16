import math

p = 3
q = 7
n = p * q                   
phi = (p - 1) * (q - 1)      

e = 2
while math.gcd(e, phi) != 1:
    e += 1

d = pow(e, -1, phi)

print("Public key: ", (e, n))
print("Private key:", (d, n))

msg = 11
C = pow(msg, e, n)  
print("Encrypted message:", C)

M = pow(C, d, n)    
print("Decrypted message:", M)
