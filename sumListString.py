# Python program to find sum of list with different
# types.

list1 = [12, 'geek', 2, '41', 'for', 10, '8', 6, 4, 'geeks', 7, '10']
    # returning sum of list using List comprehension
    #return sum([int(i) for i in l if type(i) == int or i.isdigit()])
sum = 0
for i in list1 :
 if type(i )== int or i.isdigit():
     sum =sum+int(i)

# Result of sum of list
print(sum)




# Python program to find sum of list with different
# types.
li = "abcd234"
print(list(li))
sum = 0
for i in (list(li)) :
    if (i >= '1' and i <= '9'):
     print(i)
     sum =sum+int(i)

print(sum)


sum =0
li = [1,2,3,10]
for i in li:
    sum= sum+i
    
print(sum)


li="abcd123"
for i in list(li):
    if i >='a' and i<= 'z':
        print(i,end='')