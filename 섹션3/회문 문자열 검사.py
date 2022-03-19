n=int(input())
result=[]
for i in range(n):
    s=input()
    s=s.lower()
    if s==s[::-1]:
        result.append(1)
    else:
        result.append(0)

for i in range(len(result)):
    if result[i]==1:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))