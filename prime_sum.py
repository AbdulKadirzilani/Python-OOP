from math import sqrt

T = int(input())

for _ in range(T):
    N = int(input())

    sum = 0

    if N < 2:
        pass
    elif N == 2:
        sum= 2
    else:
        sum= 2

        for number in range(3, N + 1, 2):
            

            for odd in range(3, int(sqrt(number)) + 1, 2):
                if (number % odd) == 0:
                    break
            else:  # no break
                sum+= number

    print(sum)