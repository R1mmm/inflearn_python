a=int(input())
aList=list(map(int,input().split()))
b=int(input())
bList=list(map(int,input().split()))
p1=0
p2=0
result=[]
while p1<a and p2<b:
    if aList[p1]<bList[p2]:
        result.append(aList[p1])
        p1=p1+1
    else:
        result.append(bList[p2])
        p2=p2+1

if p2==b:
    result=result+aList[p1:]
else:
    result=result+bList[p2:]


for x in result:
    print(x,end=" ")