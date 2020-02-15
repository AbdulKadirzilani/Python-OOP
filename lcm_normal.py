# Python Program to find LCM of Two Numbers using Functions
def findlcm(a, b):  # Function definition
    if (a > b):
        maximum = a
    else:
        maximum = b
    while (True):
        if (maximum % a == 0 and maximum % b == 0):
            lcm = maximum;
            break;
        maximum = maximum + 1
    return lcm


# Taking inputs from the user
num1 = int(input())
num2 = int(input())
lcm = findlcm(num1, num2)  # Function call
print(lcm)