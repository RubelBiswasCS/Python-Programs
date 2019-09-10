m=int(input("Enter number off row : "))
s=m-1
l=m

for i in range(0,m,1):
    for j in range(0,m,1):
        if j<s :
            print(" ",end="")
        else :
            print("*", end="")

        if(j==m-1):
            print('\n',end="")

    s = s-1
    m=m+1
