m=int(input("Enter number off row : "))
n=1

for i in range(0,m,1):
    for j in range(0,n,1):
        print("*",end="")
        if(j==n-1):
            print('\n',end="")
    n=n+1
