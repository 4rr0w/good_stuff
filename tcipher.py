
import math

text = str(input('enter the string you wanna encrypt/decrypt : '))
key = int(input('enter they key : '))
crypt = int(input('''1. encrypt  or 2. decrypt  : '''))

def crypt_it(string,key):
	result = [''] * key
	for i in range(len(string)):
		result[i % key] += string[i]

	return ''.join(result)

if crypt == 1:
	print(crypt_it(text,key))
elif crypt == 2:
	print(crypt_it(text,math.ceil(len(text) / key)))
else:
	print('Invalid option.')