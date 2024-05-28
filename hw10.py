import os
filename='score.bin'

def input_score(filepath):
    i=1
    score=1
    while True:
        score=int(input(f'#{i}? '))
        if score>=0:
            with open(filepath,'a') as file:
                file.write(f'{score}\n')
        else:
            break
        i+=1
    return i

def load_data(filepath):
    scores=[]
    with open(filepath,'r') as file:
        for line in file:
            scores.append(line.strip())
    return scores

def get_average(filepath,i):
    sum=0
    with open(filepath,'r') as file:
        for line in file:
            sum+=int(line.strip())
    return sum/i

def prints(filepath):
    scores=load_data(filepath)
    print('\n[점수 출력]')
    print('개인점수:',end=' ')
    for line in scores:
        print(f'{line}',end=' ')
    print()
    avg=get_average(filename,len(scores))
    print('평균: ',end='')
    print(f'{avg:.1f}')

if os.path.exists(filename):
    print('[파일 읽기]')
    prints(filename)
    
else:
    count=input_score(filename)
    prints(filename)
    
        
                  
        
