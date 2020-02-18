li = "hellowww"

#li = [1,1,1,2,2,2,2,3]

dic ={}
for i in li:
    dic[i] = li.count(i)
n =[]
print(dic)
# print(max(dic.values()))
# for k,v in dic.items():
#        if v> 1:
#          print(f"{k} ={v}")

max2=max(dic.values())
for k, v in dic.items():

    if v == max2:
        print(f"{k} ={v}")

print(dic)

print(dic.items())

print(dic.keys())
print(dic.values())

