n=8
a= [n if n%2==0 else "odd"]

print(a)

# 1 -100 even no

a= [f"{i} is Even" if i%2==0 else f"{i} is odd" for i in range(10)]

print('\n'.join(a))
#print(a)