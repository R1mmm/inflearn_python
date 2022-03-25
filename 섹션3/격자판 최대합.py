n=int(input())
arr=[]
arr2=[]
arr3=[0,0]
for i in range (n):
    a=list(map(int,input().split()))
    arr.append(a)
    arr2.append(0)

num=0
#행의 합 중에서 체크
for i in range (n):
    if num<sum(arr[i]):
        num=sum(arr[i])

#arr2 => 열의 합 / arr3 => 두 대각선의 합
for i in range (n):
    for j in range(n):
        arr2[j]+=arr[i][j]
    arr3[0]+=arr[i][i]
    arr3[1]+=arr[i][n-i-1]

#print(arr2)
#print(arr3)
result=[]
result.append(max(arr2))
result.append(max(arr3))
result.append(num)

print(max(result))
