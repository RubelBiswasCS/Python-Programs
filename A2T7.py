n=int(input("Enter number off row : "))
m=int(input("Enter number off column : "))

for i in range(0,n,1):
    for j in range(0,m,1):

        if i == 0 or i == n-1:
            print("*", end="")
        else:
            if j == 0 or j == m-1:
                print("*", end="")
            else:
                print(" ", end="")
        if (j == m - 1):
            print("\n", end="")
