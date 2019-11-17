#请使用者输入商品和价格
products = []
while True:
	name = input('请输入名称：')
	if name == 'q':
		break
	price = input('请输入价格：')
	products.append([name, price])
print(products)

print(products[0][0]) 

for p in products:
	print(p[0], '的价格是', p[1])

#写入文档，csv，txt等
with open('products.csv', 'w', encoding = 'utf-8') as f: # 写入时，选择编码utf-8
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')  #字串和数字不能做+，*运算，如果是数字，需要写成 str(p[1])
# 读取时选择编码，excel -> Data -> Get External Data -> From Text -> "选编码", next -> "选Delimiters" -> ...

#读取文档
new_products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,价格' in line:
			continue  # 继续---跳到下一循环
		name, price = line.strip().split(',')
		new_products.append([name, price])
print(new_products)
