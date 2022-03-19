n=int(input())
a=list(map(int,input().split()))
tmp=0
score=0
for i in range (len(a)):
    if a[i]==1:
        tmp=tmp+1
        score=score+tmp
    else:
        tmp=0


print(score)

