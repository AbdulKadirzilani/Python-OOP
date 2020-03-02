# #max
#
# li = [1,4,2,6,3,100]
#
# max = li[0]
#
# for i in range(len(li)):
#     if li[i]>max:
#         max=li[i]
#     else:
#         max= max
#
# print(max)


# li = [1,4,2,6,3,100]
#
# max = li[0]
#
# for i in range(len(li)):
#     if li[i]>max:
#         max=li[i]
#     else:
#         max= max
#
# print(max)

#LCD GCD
#
# a,b =3,6
# p,q=a,b
#
# while(b!=0):
#     c= a%b
#     a=b
#     b=c
# print(f"gcd = {a}")
# #print(b)
#
# lcm=(p*q)/a
#
# print(lcm)

# #factorial
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n * fact(n-1)
# a=fact(5)
# print(a)

#fibonakki
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

a=fibo(4)
print(a)
print("Fact withOut function")
fact=1
for i in range(1,6):
    fact =fact*i
print(fact)