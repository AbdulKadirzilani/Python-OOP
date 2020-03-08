# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
    # number of spaces
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=
                  " ")

            # decrementing k after each loop
        k = k - 1
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

            # ending line after each row
        print("\r")

    # Driver Code


n = 4
triangle(n)