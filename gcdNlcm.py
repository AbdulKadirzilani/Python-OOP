# Python code to demonstrate naive
# method to compute gcd ( recursion )

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

print("The gcd of 60 and 48 is : ", end="")
print(gcd(60, 30))


# from input

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD is: ")
print(GCD)
