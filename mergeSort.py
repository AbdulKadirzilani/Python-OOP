def mergeSort(list):
    #print("Splitting ", list)
    if len(list)>1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while len(left)>i and len(right)>j:
            if left[i] < right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
            k=k+1

        while len(left)>i:
            list[k]=left[i]
            i=i+1
            k=k+1

        while len(right)>j:
            list[k]=right[j]
            j=j+1
            k=k+1
    #print("Merging ", list)

nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
print(nlist)
