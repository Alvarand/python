import re, sys


fstr, sstr = sys.argv[1], sys.argv[2]
pat = re.sub(r'\*', '.*', sstr)
res = re.search(r'^' + pat + '$', fstr)
if res:
	print('ОК')
else:
	print('КО')