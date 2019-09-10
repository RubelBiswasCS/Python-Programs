m=int(input("Enter number off row : "))
n=1
i=0
sp=m2=m

while(n<m+m):
    n+=1

    while(i<m2):

        if(i<sp-1):
            print(" ", end="")
        else:
            print("*", end="")
        if(i==m2-1):
            print()

        i += 1

    i=0
    if n<=m:
        sp-=1
        m2+=1
    else:
        sp += 1
        m2 -= 1




