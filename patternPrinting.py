n = int(input("Enter a row Number: "))
for x in range(n+1):
    for y in range(n-x):
        print(" ",end="")
    for z in range(x):
        print("*",end="")
    print()