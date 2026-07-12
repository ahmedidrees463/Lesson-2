snack_name="Chocolate"
price=1.50
quantity=10
is_availble=True

print("snack:",snack_name)
print("price:",price)
print("quanity:",quantity)
print("is_availble:",is_availble)

total=price*quantity
print("total value:",total)
print("sale price:",price-0.25)
print("double stock:",quantity*2)

print("is price under $ 2:",price<2)
print("more than 5 in stock:",quantity>5)
print("is price exactly same 1.50",price==1.50)

shop="Quick"+" "+"wipes"
print("shop:",shop)
print("Letters in shop:",len(shop))
print("Frist letter:",shop[0])

temp=price
price=quantity
quantity=temp
print(price)
print(quantityf)