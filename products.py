products = []
while True:
	name = input('Please enter the name of your commodity:')
	if name == 'q': #quit
		break
	price =  input('Please enter the price of your commodity:')
	commodity = []
	commodity.append(name)
	commodity.append(price) #第7到9行可寫成commodity = [name, price]
	products.append(commodity)
print(products)

for product in products:
	print(product[0], '的價格是', product[1])

#product[0][0] 大清單中的第零格中小清單的第零格