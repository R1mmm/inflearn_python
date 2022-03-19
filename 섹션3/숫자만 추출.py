s=input()
result=""
for i in range(len(s)):
    if ord(s[i])>=48 and  ord(s[i])<=57:
        result=result+s[i]

result=int(result)

count=0
for i in range (1,result+1):
    if result%i==0:
        count+=1

print(result)
print(count)