
#创建一个函数，将参数列表中每个元素都变为大写
def high(l):
	return[i.upper() for i in l]


#创建高阶函数，接受一个函数和一个列表作为参数
def test(h,l):
	return h(l)

l = ['wuhan','hut','china']

print(test(high,l))
