n=int(input())

a=list(map(int,input().split()))
ori=a[:]
result=[]
for i in range(len(a)):
    result.append(0)
    while a[i]>0:
        result[i]=result[i]+a[i]%10
        a[i]=int(a[i]/10)
    
print(ori[result.index(max(result))])