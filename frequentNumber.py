li = [1,2,3,3]
print(li.count(2))

str="hellow"

dic={}
for x in str:
    if x in dic.keys():
        dic[x]+=1
    else:
        dic[x]=1
print(dic)

a = max(dic, key=dic.get)
print(a)



numbers = [1,1,2,3,1,4,5,2,2,2]
print(max(set(numbers), key=numbers.count))
#print(li.count.keys())