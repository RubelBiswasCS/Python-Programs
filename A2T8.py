m=int(input("Enter number off row : "))
n=1

for i in range(0,m,1):
    for j in range(0,n,1):

        if i == 0 or i == 1 or i == m-1:
            print("*", end="")
        else:
            if j == 0 or j == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        if (j == n - 1):
            print("\n", end="")
    n=n+1
