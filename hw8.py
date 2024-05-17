def dict_get(dic,key):
    if key in dic:
        return dic[key]
    else:
        return None
    
def buy(shopping_bag):
    while True:
        print('[구입]')
        n=str(input('상품명? '))
        if n=='':
            return False
        p=int(input('수량은? '))
        shopping_bag[n]=p
        print(f'장바구니에 {n} {p}개가 담겼습니다.')
        print()
        
def show(s):
    print(f'>>> 장바구니 보기: {s}')
    
def find(s):
    i=str(input('장바구니에서 확인하고자 하는 상품은? '))
    res=dict_get(s,i)
    if i in s:
        print(f'{i}은(는) {res}개 담겨 있습니다.')
        
shopping_bag={}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)

print('[검색]')
find(shopping_bag)
