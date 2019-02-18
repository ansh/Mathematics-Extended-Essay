d = 13
n = 77

private_key = [d,n]

ciphertext = [17,66]


def decrypt(c):
	return pow(c, private_key[0], private_key[1])

for i in ciphertext:
	print(decrypt(i))