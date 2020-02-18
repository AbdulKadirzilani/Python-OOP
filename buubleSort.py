li = [64, 34, 25, 12, 22, 11, 90]


for i in range(len(li)):
    for j in range(len(li)-i-1):

        if li[j]> li[j+1]:
            tem= li[j]
            li[j]=li[j+1]
            li[j+1] =tem


print ("Sorted array is:")
for i in range(len(li)):
    print (li[i])