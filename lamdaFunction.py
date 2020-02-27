
# lamda function n name function

def square(a,b): # here square is name function

    return a*a+2*a*b+b*b

s = square(2,3)

print(s)

print()

# lambda function has no name
#work single expression/single line of code

s= (lambda a,b:a*a+2*a*b+b*b)(2,3)
print(s)

