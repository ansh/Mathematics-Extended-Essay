e = 37
n = 77

public_key = [e,n]

plaintext = input("Enter a message: ")
plaintext = list(plaintext)

print(ord(plaintext[1]))

def encrypt(p):
	return pow(p, public_key[0], public_key[1])

for i in plaintext:
	print(encrypt(ord(i)))