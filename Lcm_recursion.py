# Python Program to find the LCM of Two Numbers using Recursion
def findgcd(a, b):   # Function definition
    if(b == 0):
        return a;
    else:
        return findgcd(b, a % b)   # Recursion takes place here
num1 = int(input())
num2 = int(input())
gcd = findgcd(num1, num2)   #function call
lcm = (num1 * num2) // gcd
print(lcm)