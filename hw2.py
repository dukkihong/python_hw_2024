def exchange(cost):
    five_hundred=cost//500
    cost=cost%500
    one_hundred=cost//100
    cost=cost%100
    fifty=cost//50
    cost=cost%50
    ten=cost//10
    print("500원 동전의 개수: ",five_hundred)
    print("100원 동전의 개수: ",one_hundred)
    print("50원 동전의 개수: ",fifty)
    print("10원 동전의 개수: ",ten)

def get_integer():
    cost=int(input("동전으로 교환하고자 하는 금액은? "))
    return cost

cost=get_integer()
exchange(cost)
