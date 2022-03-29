import copy
arr1=[list(map(int,input().split())) for _ in range(9)]
num=[1,2,3,4,5,6,7,8,9]
arr=copy.deepcopy(arr1)
arr2=[]
arr3=[[],[],[],[],[],[],[],[],[]]
for i in range(9):
    #arr2.append([])
    temp=list(arr1[k][i] for k in range(9))
    arr2.append(temp)

temp=[]

for i in range(9):
    for j in range(3):
        if i<3:
            temp+=arr1[j][:3]
            if j==2:
                arr3[i]=arr3[i]+temp
                temp=[]
            del arr1[j][:3]
        elif i>=3 and i<=5:
            temp+=arr1[j+3][:3]
            if j==2:
                arr3[i]=arr3[i]+temp
                temp=[]
            del arr1[j+3][:3]
        else:
            temp+=arr1[j+6][:3]
            if j==2:
                arr3[i]=arr3[i]+temp
                temp=[]
            del arr1[j+6][:3]

#print(arr1)
#print(arr2)
#print(arr3)
#print(arr)

#and arr2[i] and arr3[i]

count=0
for i in range(9):
    if all(num[k] in arr[i] for k in range(9)):
        count+=1
    if all(num[k] in arr2[i] for k in range(9)):
        count+=1
    if all(num[k] in arr3[i] for k in range(9)):
        count+=1

#print(count)
if count==27:
    print('YES')
else:
    print('NO')
"""
for i in range(9):
    if all(num[k] in arr1[i] for k in range(9)):
        continue
    if all(num[k] in arr1[k][i] for k in range(9)):
        continue
    else:
        print("NO") 
        break
"""