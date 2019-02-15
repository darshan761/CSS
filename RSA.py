import random,math,sympy

ch = 1
while ch==1 :
	P = int(input("Enter value of P:"))
	Q = int(input("Enter value of Q:"))

	if sympy.isprime(P) and sympy.isprime(Q):
		ch = 2
	else:
		print("P and Q should be prime numbers")
		

n = P*Q
phi = (P-1)*(Q-1)
E = []
d = 1
for i in range(2,phi):
    if math.gcd(i, phi)==1 :
        E.append(i)

print(E)
e = random.choice(E)
while (e*d)%phi!=1 :
    d = d+1
    if d==phi :
    	e = random.choice(E)

print("Public Key:",e,"\nPrivate Key:",d)
PT =[]
ciph=[]
deciph = []
PT = input("Enter plain Text:")
for j in PT :
    c = ord(j)
    cipher = (c**e)%n
    ciph.append(cipher)

print("Encrypted:",ciph)
for j in ciph:
    print(chr(j),end='')

print("\n")
for j in ciph:
    deciph.append((j**d)%n)

print("Decrypted:",deciph)

for j in deciph:
    print(chr(j),end='')
