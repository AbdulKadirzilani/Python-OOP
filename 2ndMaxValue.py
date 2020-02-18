dic ={ 'a':2,'b':4,'c':1}

max = max(dic.values())
print(max)
max2=0
for i in dic.values():
    if i >max2 and i <max:
        max2=i
print(max2)