def read_single_digit(num):
    if num==0:
        return '영'
    elif num==1:
        return '일'
    elif num==2:
        return '이'
    elif num==3:
        return '삼'
    elif num==4:
        return '사'
    elif num==5:
        return '오'
    elif num==6:
        return '육'
    elif num==7:
        return '칠'
    elif num==8:
        return '팔'
    else:
        return '구'

def read_number(num):
    res=""
    st=str(num)
    for i in range(len(st)):
        n=int(st[i])
        a=read_single_digit(n)
        res+=a
        res+=' '
    return res

num=int(input("세 자리 정수 입력: "))
print(read_number(num))
