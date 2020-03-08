li=[1, 2, 3, 5, 8]
first = 0
last = len(li) - 1
    #found = False
key=8
while (first <= last):
        mid = (first + last) // 2
        if li[mid] == key:
            print(f"{li[mid]} is found and position={mid}")
            break
        elif li[mid]>key:
                last = mid - 1
        elif li[mid]<key:
                first = mid + 1

else:
    print("Not found")

