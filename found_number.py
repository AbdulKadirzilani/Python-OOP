# li = [2,3,4,9]
#
# if 9 in li:
#
#     print("found")
# else:
#     print("Not found")
#


li = [2,3,4,9]
#print(len(li))
j=-1
for i in range(len(li)):
    if li[i] == 2:
       j = i+1
       break

if j==-1:
    print("Not found")
else:
    print(f"found={li[i]}. The position= {j}.")