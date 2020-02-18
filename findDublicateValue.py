

li = [2,3,4]
result = set(li)

print(result)
my_list = [1,2,2,4,3,3]
my_list.sort()
print(my_list)
print(len(my_list))
count = 0
for i in range (len (my_list)-1):
    if my_list[i] == my_list[i+1]:
            count+=1
            print(my_list[i])
print(count)



def most_frequent(List):
    return set(List)

#list=[1,2,2,3]
List = [2,2,4]
print(most_frequent(List))