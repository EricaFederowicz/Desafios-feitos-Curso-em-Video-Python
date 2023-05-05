def fatorial(n,show=True):
    f = n
    if show == True:
        print(n, end=' ')
    for i in range(n-1):
        n -= 1
        f *= n
        if show == True:
            print('x',n,end=' ')
    print('=',f)


fatorial(5)
print('FIM')






