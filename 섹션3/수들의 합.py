#스스로 다시 꼭 풀어볼것

n,m=map(int,input().split())
arr=list(map(int,input().split()))
lt=0
rt=1
count=0
tot=arr[0]
while True:
    if tot<m:
        if rt<n:
            tot+=arr[rt]
            rt+=1
        else:
            break
    elif tot==m:
        count+=1
        tot-=arr[lt]
        lt+=1
    else:
        tot-=arr[lt]
        lt+=1

print(count)


"""
내가 짠 코드...결과값이 다름
result=[]
i=-1
count=0
sum=0
temp=[]
while i<n:
    if i==n-1 and arr[i]!=m and sum!=m:
        break
    i+=1
    if sum==m:
        count+=1
        #result.append(i)
        sum=0
        i=temp[0]
        temp=[]
    elif sum>m:
        sum=0
        i=temp[0]
        temp=[]
    else:
        sum=sum+arr[i]
        temp.append(i)
        #if i<n-1:

print(count)
#print(result)
"""
