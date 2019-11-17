#Refactor products.py 重构

import os # operating system

#读取文档
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue  # 继续---跳到下一循环
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

#写入文档
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: # 写入时，选择编码utf-8
		f.write('商品,价格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')  


#请使用者输入，在给入的参数products后面添加新的[name, price]
def user_input(products):
	while True:
		name = input('请输入名称：')
		if name == 'q':
			break
		price = input('请输入价格：')
		products.append([name, price])
	return products

#印出商品和价格
def print_products(products):
	for p in products:
		print(p[0], '的价格是', p[1])

def main():
	if os.path.isfile('products.csv'):
		print('找到档案了！')
		products = read_file('products.csv')  #先将products.csv原有内容读到products里
		user_input(products)   #再将新输入的内容续在products后
		print_products(products)
		write_file('products.csv', products)  #写入时，会覆盖掉products.csv原有内容
	else:
		print('找不到档案……')

main()
