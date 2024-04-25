i=2
while(i<7):
    if(i==2 or i==6):
        for j in range(1,10,1):
            for k in range(0,4,1):
                print(f"{i+k}x{j}={(i+k)*j:2d}",end='   ')
            print()
        print()
    i+=1
    
