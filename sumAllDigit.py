
# int obj is not iterable

n =123
s1 = str(n)
sum=0
for i in s1:
    sum= sum+ int(i)
print(sum)


n ="123"
s1 = list(n)
sum=0
for i in s1:
    sum= sum+ int(i)
print(sum)




sum =0
li = [1,2,3,4]
for i in li:

    sum +=i
print(sum)