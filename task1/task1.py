import sys


def main():
	print(itoBase(*sys.argv[1:]))


def itoBase(nb:str, base:str, baseDst:str=False):
	dictionary = {'0' : '0', '1' : '1', '2' : '2', '3' : '3', '4' : '4', '5' : '5', '6' : '6', '7' : '7', '8' : '8', '9' : '9', '10' : 'a', '11' : 'b', '12' : 'c', '13' : 'd', '14' : 'e', '15' : 'f'}
	reverseDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'a' : 10, 'b' : 11, 'c' : 12, 'd' : 13, 'e' : 14, 'f' : 15}
	SI = ['01', '012', '0123', '01234', '012345', '0123456', '01234567', '012345678', '0123456789', '0123456789a', '0123456789ab', '0123456789abc', '0123456789abcd', '0123456789abcde', '0123456789abcdef']
	fFlag = base.lower() in SI
	if baseDst:
		sFlag = baseDst.lower() in SI
		if nb == '0':
			return '0'	
		if fFlag and sFlag:
			baseSrc = len(base) # СИ из которой нужно перевести
			baseTo = len(baseDst) # СИ в которую нужно перевести
			i = 0 # Счетчик
			number = 0 # Число в десятичной СИ
			while nb:
				number += reverseDict[nb[-1].lower()] * baseSrc ** i
				i += 1
				nb = nb[:-1]
			result = '' # Результирующая на вывод
			while number > 0:
				result = dictionary[str(number % baseTo)] + result
				number = number // baseTo
			return result
		else:
			return 'usage'
	else:
		nb = abs(int(nbs))
		if nb == 0:
			return '0'	
		if fFlag:
			baseTo = len(base) # СИ в которую нужно перевести
			result = '' # Результирующая на вывод
			while nb > 0:
				result = dictionary[str(nb % baseTo)] + result
				nb = nb // baseTo
			return result
		else:
			return 'usage'


if __name__ == '__main__':
	main()