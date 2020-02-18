#153
n =153

s1 = str(n)
sum=0
count =0
for i in s1:
    a=int(i)
    sum = sum+a*a*a
    count+=1
print(sum)
print(count)
if sum==n:
    print(n, "is armStrong")