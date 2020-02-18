s1=[1,2,3]
s2 = []
print(len(s2))

if (len(s2)==0):
    while(len(s1)!=0):
        s2.append(s1.pop())
s2.pop()


print(s2)

k=[2,3,4]
for i in range(len(k)):
    k.pop()
print(k)


s1=[1,2,3]
s2 = s1[::-1]
print(s2)
