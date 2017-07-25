from math import sqrt

def reverse(num):
	reverse = ''
	for i in range(len(num), 0, -1):
		reverse += num[i-1]

	return reverse

def toNumber(b):
	b = reverse(b)
	b = list(b)
	print(b)

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
	values = []
	for asci in s:
		values.append(chr(asci))
	return ''.join(values)

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
		
while True:
	#x = toNumber(input("Binary: "))

	#x = convertToBinary(int(input("Number: ")))
	#print(int(''.join(num)))
	#num = []

	#x = wordToAscii(input("Word: "))
	#print(AsciiToWord(x))
	print(wordToBinary(input("Word: ")))


