

li = "abc23d"
li2=[]
sum=0
for i in li:
    if (i>='1' and i<='9'):
        li2.append(i)
        #sum=sum+i
print(li2)
for i in li2:
 #if type(i )== int or i.isdigit():

 if (i >= '1' and i <= '9'):
     sum =sum+int(i)

# Result of sum of list
print(sum)

print(''.join(li2))


print(li,end='')