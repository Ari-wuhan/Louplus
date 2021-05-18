# 打开并读取文件里的字符串
with open('/tmp/String.txt') as f:
	s = f.read()
	sum =' '
	for i in s:
		if i.isdigit():
			sum +=  i
	print(sum)
