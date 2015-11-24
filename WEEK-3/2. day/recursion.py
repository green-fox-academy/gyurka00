def f(n):
    if n==0:
        return
    print ("hello")
    f(n-1)

f(5)

def fibon(n):
    if n==0:
        return 0
    if n==1:
        return 1

    return fibon(n-1)+fibon(n-2)



print (fibon(4))
