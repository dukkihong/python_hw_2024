def show_name(name):
    msg1=f"Hello {name},"
    msg2="Welcome to Seoul."
    if(len(msg1)>len(msg2)):
        nstr=len(msg1)
    else:
        nstr=len(msg2)
    print('-'*(nstr+2))
    print(msg1)
    print(msg2)
    print('-'*(nstr+2))

name=input("Input his/her name: ")
show_name(name)
