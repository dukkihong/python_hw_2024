def get_fixed_price(sale,price):
    origin=int(price/(100-sale)*100)
    return origin

sale_rate=int(input("할인율은? "))
A_price=int(input("A 상품의 할인된 가격은? "))
B_price=int(input("B 상품의 할인된 가격은? "))
A_origin=get_fixed_price(sale_rate,A_price)
B_origin=get_fixed_price(sale_rate,B_price)
print("A 상품의 정가는",A_origin,"원")
print("B 상품의 정가는",B_origin,"원")
