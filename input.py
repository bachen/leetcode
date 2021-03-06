import re

def input():
	filename = 'input.txt'
	try:
		fp = open(filename,'r')
	except:
		print 'fail to open input.txt . check it whether exists.'
		return False

	try:
		f = fp.read()
	except:
		print 'fail to read input.txt .'
		return False
	finally:
		fp.close()

	if f == '':
		print 'There is no content in input.txt .'
		return False

	final_f = f.splitlines()
	content = []
	[content.append(line.rstrip('\n').strip(' ')) for line in final_f]

	result = []

	#+123,123,-123,+1.2,-0.0, except 01. 
	pattern0 = re.compile(r'^[+-]?\d+\d$|^[+-]?\d+\.\d+')
	match = pattern0.match(content[0])
	if match:
		result.append(float(match.group()))
	else:
		result.append(None)
	
	#[12,23,34]
	tmp_list = []
	pattern1 = re.compile(r'^\[(\d+\,)*(\d+)\]$')
	match = pattern1.match(content[1])
	if match:
		tmp = match.group().lstrip('[').rstrip(']').split(',')
		tmp_list = [int(i) for i in tmp]
		result.append(tmp_list)
	else:
		result.append(None)

	#[12.3,23,34.0]
	tmp_list = []
	pattern2 = re.compile(r'^\[(\d+\,|\d+\.\d+\,)*(\d+|\d+\.\d+)\]$')
	match = pattern2.match(content[2])
	if match:
		tmp = match.group().lstrip('[').rstrip(']').split(',')
		tmp_list = [float(i) for i in tmp]
		result.append(tmp_list)
	else:
		result.append(None)

	#[12.3,23,34.0]
	tmp_list = []
	pattern3 = re.compile(r'^\[(\((\d+\,)*\d\)\,)*(\((\d+\,)*\d\))\]$')
	match = pattern3.match(content[3])
	if match:
		tmp = match.group().lstrip('[').lstrip('(').rstrip(']').rstrip(')').split('),(')
		for i in tmp:
			tmp = i.split(',')
			ttmp = []
			for j in tmp:
				ttmp.append(int(j))
			tmp_list.append(tuple(ttmp))
		result.append(tmp_list)
	else:
		result.append(None)
	return result

if __name__=='__main__':
	if input():
		print input()
	else:
		print 'Your testcase should be modified.'