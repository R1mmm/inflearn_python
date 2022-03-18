n=int(input())
a=list(map(int,input().split()))
avg=round(sum(a)/n)

std=100

for idx,x in enumerate(a):
    tmp=abs(x-avg)
    if tmp<std:
        std=tmp
        score=x
        res=idx+1
    elif tmp==min: #편차는 같으나 점수가 더 큰 경우
        if x>score:
            score=x
            res=idx+1

print(avg,res)


