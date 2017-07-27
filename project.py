from math import sqrt

def reverse(num):
	reverse = ''
	for i in range(len(num), 0, -1):
		reverse += num[i-1]

	return reverse

def toNumber(b):
	b = reverse(b)
	b = list(b)

	count = 1
	change = 1
	amount = 0

	for num in b:
		if(int(num) == 0):
			change = change*2
		else:
			amount = amount + (change*int(num))
			change = change*2

	return amount

num = []
def convertToBinary(n):
	if n > 1:
		convertToBinary(n//2)
	num.append(str(n % 2))

def wordToAscii(s):
	values = []
	for word in s:
		values.append(ord(word))
	return values

def AsciiToWord(s):
	return chr(s)

def AsciiToBinary(s):
	values = []
	for asci in s:
		values.append(bin(asci))
	return values

def wordToBinary(s):
	values = []
	for asci in s:
		values.append(bin(ord(asci)).replace("0b",""))
	return values


def xorGate(m, k):
	string = ""
	index = 0
	for num in m:
		if(k[index] == num):
			string += "1"
		else:
			string += "0"
		index = (index+1)%len(k)
	if(toNumber)
	print(toNumber(string))
	return string

# ' " \k ...

from random import randint

def Xorcipher(mes, key):

	value = []
	engli = []
	for c in mes:
		value.append(xorGate(wordToBinary(c)[0], key))

	for val in value:
		engli.append(AsciiToWord(toNumber(val)))




	print(engli)
	return ''.join(engli)


key = ""
for c in range(7):
	key += str(randint(0,1))

print(Xorcipher(input("Encrypt string here: "), key))
print(Xorcipher(input("Decrypt string here: "), key))
