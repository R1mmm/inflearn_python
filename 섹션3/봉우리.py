n=int(input())
a=[list(map(int,input().split())) for _ in range (n)]
temp=[]
count=0
for i in range (n+2):
    temp.append(0)
for i in range(n):
    a[i].append(0)
    a[i].insert(0,0)

a.insert(0,temp)
a.append(temp)

#print(a)

for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j] and a[i][j]>a[i][j-1] and a[i][j]>a[i][j+1]:
            count+=1


print(count)

"""
a=temp+a+temp
count=0
for i in range(n):
    for j in range (n):
        """