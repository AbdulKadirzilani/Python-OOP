def gen(n):

    i = 0
    while(i<n):
        yield i
        i+=1
x = gen(10)

for item in x:
    print(item)