def faktorial(n, stack=[]):
    if n == 0:
        return 1
    else:
        stack.append(n)
        return n * faktorial(n-1, stack)

print(faktorial(7))  
