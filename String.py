#title() upper() lower()  swapcase() isalnum() isalpha() split() join()  strip()剥离字符串
s = 'wuhan is a wonderful boy,with the best luck'

t = s.title()#以标题形式
u = s.upper()#全变大写
l = s.lower()#变小写
swa = s.swapcase()#大小写交换
aln = s.isalnum()#全为字母和数字？
alp = s.isalpha()#全为字母？
spl = s.split()#分割
joi = s.join('nice')#链接字符

print(t)
print(l)
print(swa)
print(aln)
print(alp)
print(spl)
print(joi)
print(u)
print(s.strip())
print(s.lstrip())
print(s.rstrip())


#文本搜索
#find() startswith()  endswith()

print(s.find('wuhan'))
print(s.startswith('wu'))
print(s.endswith('wu'))



