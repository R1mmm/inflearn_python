#혼자서 다시 꼭 풀어볼 것!

n=int(input())

arr=[list(map(int,input().split()))for _ in range (n)]
res=0
s=e=n//2

for i in range(n):
    for j in range (s,e+1):
        res+=arr[i][j]

    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(res)