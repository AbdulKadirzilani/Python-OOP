li = [5,10,2,8,7]


for i in range(len(li)): #5
    for j in range(len(li)-i-1): #3

        if li[j]> li[j+1]:
            tem= li[j]
            li[j]=li[j+1]
            li[j+1] =tem


print ("Sorted array is:")
for i in range(len(li)):
    print (li[i])