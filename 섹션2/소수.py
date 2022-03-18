n=int(input())

"""
처음에 내가 구현한거 , , , 시간 초과남.
count=0
result=0
for i in range (2,n+1):
    for j in range (1,i+1):
        if i%j==0:
            count=count+1
        if count>2:
            break
        
    if count<3:
        result=result+1
    count=0

print(result)
"""
result=0
arr=[0]*(n+1)
for i in range (2,n+1):
    if arr[i]==0:
        result+=1 #소수에 추가
        #arr[i]+=1
        j=i
        t=2
        while j*t<n+1: #2의배수인 4는 이미 1이 되어서 다음엔 체크 안 하도록!
            if arr[j*t]==0:
                arr[j*t]+=1
            t=t+1
print(arr.count(0)-2)

