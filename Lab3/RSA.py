import math

#step 1
p = 3
q = 7

#step 2
n = p*q
phi = (p-1)*(q-1)
e = 2


def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp
        

while (e < phi):
    if(gcd(e, phi) == 1):
        break
    else:
        e = e+1
        

#step 3
k = 2
d = (1 + (k*phi))/e



#step 4
msg = 12.0
 
print("Message data = ", msg)
 
c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)
 
 #step 5
 
# Decryption m = (c ^ d) % n
m = pow(c, d)
m = math.fmod(m, n)
print("Original Message Sent = ", m)
