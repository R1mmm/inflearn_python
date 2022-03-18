n=int(input())
a=list(map(int,input().split()))

def reverse(x):
    tmp=list(str(x))
    while tmp[-1]=='0':
        del tmp[-1]
    tmp=tmp[::-1]
    tmp=''.join(tmp)

    return int(tmp)

def isPrime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count=count+1
    if count>2 or x==1:
        return 0
    else:
        return 1

result=[]
for i in range(n):
    result.append(0)
    a[i]=reverse(a[i])
    result[i]=isPrime(a[i])

for i in range(n):
    if result[i]==1:
        print(a[i], end=" ")