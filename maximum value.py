a=[]

for i in range(1,6):
     n = int(input())
     a.append(n)

print(a[0])
max=a[0]


for i in range(1,5):
    if a[i]>max:

        max=a[i]
print(max)