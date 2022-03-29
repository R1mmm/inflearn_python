n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
m=int(input())
for i in range(m):
    a,b,c=map(int,input().split())
    c=c%n
    if b==0:
        temp=arr[a-1][0:c]
        arr[a-1]=arr[a-1][c:]
        arr[a-1]=arr[a-1]+temp

    else:
        temp=arr[a-1][:-c]
        arr[a-1]=arr[a-1][-c:]
        arr[a-1]=arr[a-1]+temp


#print(arr)
res=0
s=0
e=n-1
count=0
for i in range(n):
    for j in range(s,e+1):
        res+=arr[i][j]
        #print(arr[i][j])
    if e>n//2 and i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1



print(res)

