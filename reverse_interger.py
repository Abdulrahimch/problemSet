def reverse(x):
    if x<0:
        rev = int(str(x).replace("-","")[::-1])*-1
    else:
        rev = int(str(x).replace("-", "")[::-1])

    if -2147483648 < rev < 2147483648:
        return rev
    else:
        return 0
print(reverse(1345))
