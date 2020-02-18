
d= {'h':2, 'a':1,'h':"ppp"}

print(d)





str="hellow"

dic={}
for i in str:
    dic[i] =str.count(i)

    #if x in dic.keys():

print(dic)

l=max(dic.values())
#print(l,keys[l])


dic= {'u':2,'v':3,'d':8}

print("d:",max(dic.values()))

# for key,value in dic.items():
#     if max(dic[value]):
#        print(key,value)
#print(max(dic.items()))


#print(li.count.keys())


# Program to find most frequent
# element in a list

def most_frequent(List):
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return (itm)


List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))