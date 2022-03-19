n=int(input())
result=[]

for i in range(n):
    tmp=input().split()
    tmp.sort()
    a,b,c=map(int,tmp)
    if a==c :
        result.append(10000+a*1000)
    else:
        if a==b:
            result.append(1000+a*100)
        elif b==c:
            result.append(1000+b*100)
        else:
            result.append(c*100)

#print(tmp)
#print(result)
print(max(result))