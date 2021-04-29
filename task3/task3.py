import sys, re
sys.stdin.reconfigure(encoding='utf-8')

'''
Ввод в командную консоль осуществляется следующим образом: 
	python task3.py < log_filename.txt first_argument second_argument
'''

def main():
	try:
		startYear = re.search(r'\d{4}-\d{2}-\d{2}', sys.argv[1]).group()
		startTime = re.search(r'\d{2}:\d{2}:\d{2}', sys.argv[1]).group()
		endYear = re.search(r'\d{4}-\d{2}-\d{2}', sys.argv[2]).group()
		endTime = re.search(r'\d{2}:\d{2}:\d{2}', sys.argv[2]).group()
		parse(startYear, startTime, endYear, endTime)
	except:
		print('usage')


def parse(startYear, startTime, endYear, endTime):
	volumeB = 0 # Объем бочки изначально
	currentV = 0 # Текущий объем
	tryTopUp = 0  # Количество попыток налить воду
	tryFailTopUp = 0 # Количество неудачных попыток
	waterTopUp = 0 # Объем налитой воды
	waterNotTopUp = 0 # Объем не налитой воды
	tryScoop = 0 # Количество попыток забора воды
	tryFailScoop = 0 # Количество неудачных попыток
	waterScoop = 0 # Объем забранной воды
	waterNotScoop = 0 # Объем не забранной воды

	for line in sys.stdin:
		if 'meta' in line.lower():
			continue
		elif 'объем бочки' in line:
			volumeB =  int(line.split()[0])
		elif 'текущий' in line:
			currentV = int(line.split()[0])
		else:
			try:
				YEAR = re.search(r'\d{4}-\d{2}-\d{2}', line).group()
				TIME = re.search(r'\d{2}:\d{2}:\d{2}', line).group()
			except:
				continue
			if endYear < YEAR or endYear == YEAR and endTime <= TIME: # Проверка на конец указанного периода
				break
			if startYear < YEAR or startYear == YEAR and startTime <= TIME: # Проверка, что время из логов входит в указанный период
				if 'top up' in line.lower():
					tryTopUp += 1
					if 'успех' in line:
						success = int(re.search(r'\d+l', line).group()[:-1])
						waterTopUp += success
						currentV += success
					elif 'фейл' in line:
						tryFailTopUp += 1
						waterNotTopUp += int(re.search(r'\d+l', line).group()[:-1])
				elif 'scoop' in line.lower():
					tryScoop += 1
					if 'успех' in line:
						success = int(re.search(r'\d+l', line).group()[:-1])
						waterScoop += success
						currentV -= success
					elif 'фейл' in line:
						tryFailScoop += 1
						waterNotScoop += int(re.search(r'\d+l', line).group()[:-1])

	print('Количество попыток налить воду:', tryTopUp)
	print('Процент ошибок: ', tryFailTopUp / tryTopUp * 100 , '%', sep='')
	print('Объем налитой воды:', waterTopUp)
	print('Объем не налитой воды:', waterNotTopUp)
	print('Количество попыток черпнуть воду:', tryScoop)
	print('Процент ошибок: ', tryFailScoop / tryScoop * 100 , '%', sep='')
	print('Объем налитой воды:', waterScoop)
	print('Объем не налитой воды:', waterNotScoop)

if __name__ == '__main__':
	main()