a=[list(map(int,input().split())) for _ in range(7)]

new_a=[]
temp=[]
for i in range(7):
    for j in range(7):
        temp.append(a[j][i])
        if j==6:
            new_a.append(temp)
            temp=[]

count=0
for i in range(7):
    for j in range(3):
        temp=list(reversed(a[i][j:j+5]))
        temp2=list(reversed(new_a[i][j:j+5]))
        if a[i][j:j+5]==temp:
            count+=1
        if new_a[i][j:j+5]==temp2:
            count+=1

print(count)