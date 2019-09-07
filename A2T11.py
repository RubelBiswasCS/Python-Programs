n = int(input("Enter value "))
m = n + n
sp = s2 = n
for i in range(1, m, 1):
    for j in range(0, sp, 1):

        if (j < n - 1):
            print(" ", end="")
        if (j == n - 1 or j == sp-1 ):
            print("*", end="")
        if (j == n - 1):
            print()
    if (i<s2):
        sp += 1
        n -= 1
    else:
        sp -= 1
        n += 1