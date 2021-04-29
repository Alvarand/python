import sys, json, re

'''
Ввод в командную консоль осуществляется следующим образом: 
	python task2.py < filename.txt
'''


def main():
	for line in sys.stdin:
		try:
			string = regexp(line)
			sjson = json.loads(string)
			solution(sjson)
		except:
			print("Что-то пошло не так!")

def regexp(string:str): # Редактирование строки под формат JSON
	l = string.find('line') # Позиция 'line' в строке
	s = string.find('sphere') # Позиция 'sphere' в строке
	if s > l:
		strline = string[:s].replace(' ', '') # Строка под прямые
		strsphere = string[s:].replace(' ', '') # Строка под сферу	
		strsphere = re.sub(r'sphere', '"sphere"', strsphere)
		strsphere = re.sub(r'center', '"center"', strsphere)
		strsphere = re.sub(r'radius', '"radius"', strsphere)
		strline = re.sub(r'line', '"line"', strline)
		strline = re.sub(r'{\[', '[[', strline)
		strline = re.sub(r'\]}', ']]', strline)
		string = strline + strsphere
	else:
		strline = string[l:].replace(' ', '') # Строка под прямые
		strsphere = string[:l].replace(' ', '') # Строка под сферу	
		strsphere = re.sub(r'sphere', '"sphere"', strsphere)
		strsphere = re.sub(r'center', '"center"', strsphere)
		strsphere = re.sub(r'radius', '"radius"', strsphere)
		strline = re.sub(r'line', '"line"', strline)
		strline = re.sub(r'{\[', '[[', strline)
		strline = re.sub(r'\]}', ']]', strline)
		string = strsphere + strline
	return string


def solution(dictionary:dict):
	cx = dictionary['sphere']['center'][0]
	cy = dictionary['sphere']['center'][1]
	cz = dictionary['sphere']['center'][2]
	r = dictionary['sphere']['radius']

	fx = dictionary['line'][0][0]
	fy = dictionary['line'][0][1]
	fz = dictionary['line'][0][2]

	sx = dictionary['line'][1][0]
	sy = dictionary['line'][1][1]
	sz = dictionary['line'][1][2]	

	vx = sx - fx
	vy = sy - fy
	vz = sz - fz

	A = vx ** 2 + vy ** 2 + vz ** 2
	B = 2 * (fx * vx + fy * vy + fz * vz - vx * cx - vy * cy - vz * cz)
	C = fx ** 2 - 2 * fx * cx + cx ** 2 + fy ** 2 - 2 * fy * cy + cy ** 2 + fz ** 2 - 2 * fz * cz + cz ** 2 - r ** 2
	D = B ** 2 - 4 * A * C
	if D < 0:
		print('Коллизий не найдено')
	elif D == 0:
		t = -B / (2 * A)
		x = fx * (1 - t) + t * sx
		y = fy * (1 - t) + t * sy
		z = fz * (1 - t) + t * sz
		print(x, y, z)
	else:
		t1 = (-B + D ** 0.5) / (2 * A)
		t2 = (-B - D ** 0.5) / (2 * A)

		x1 = fx * (1 - t1) + t1 * sx
		y1 = fy * (1 - t1) + t1 * sy
		z1 = fz * (1 - t1) + t1 * sz

		x2 = fx * (1 - t2) + t2 * sx
		y2 = fy * (1 - t2) + t2 * sy
		z2 = fz * (1 - t2) + t2 * sz

		print(x1, y1, z1)
		print(x2, y2, z2)

if __name__ == '__main__':
	main()


