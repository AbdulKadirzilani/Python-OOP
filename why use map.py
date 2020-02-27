# #iterate using function
# li = [1,2,3,4]
# for i in li:
#     print(i*i*i)
#
#

##when passing multiple value as parameter
#map is awsome for iterate multiple value

def ab(x):

    return x*x

num =[1,2,3,4]

c= list(map(ab,num))
print(c)