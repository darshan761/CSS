import random
q = int(input("Enter value of q (prime no):"))
A = []
for i in range(2,q+1):
	temp = set()
	for j in range(2,q+1):
		temp.add((i**j)%q)

	if len(temp) == q-1 :
		A.append(i)

print(A)
a = random.choice(A)
print("Root chosen:",a)
priv = []
pub = []
n = int(input("Enter no of users:"))
for i in range (1,n+1):
	print("Enter Private key for user",i,":")
	priv.append(int(input()))

print("Private keys:",priv)
for i in range(0,n):
	pub.append((a**priv[i])%q)

print("Public keys:",pub)
ch = 'Y'
while ch!='e' :
	print("Enter Users to display shared key:")
	a = int(input())
	b = int(input())
	print("Shared key for user ",a,":",pub[b-1]**priv[a-1]%q)
	print("Shared key for user ",b,":",pub[a-1]**priv[b-1]%q)
	ch = input("press enter to continue or e to exit\n")
	print("Exit Successful!")
