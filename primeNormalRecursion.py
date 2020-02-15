def prime(n):
    if n == 0:
        print("This is not a Prime number")
        answer = 0
    if n == 1:
        print("This is not a Prime number")
        answer = 1
    else:
        val1 = n // prime(n - 1)
        if val1 == 0:
            print("This is not a Prime number")
            answer = False
        else:
            print("This is a prime number")
            answer = True

    return answer