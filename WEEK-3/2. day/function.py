def great(name):
    return "hello " + name

result=great("Gyuri")
print(result)

g=[]
def add(a,b):
    res=a+b
    g.append(res)
    return res

print(add(1, 2))
print(add(6, 3))
print(g)


n=1
def my_print():
    n=2
    print(n)
print(n)
my_print()

def great(name,hello="hello"):
    return hello+ " " + name

result=great("Gyuri","csa")
print(result)
result2=great("Gyuri")
print(result2)


def add(a, b, res= None):
    if res is None:
        res=[]
    r=a+b
    res.append(r)
    print(res)
    return r

add(1,2)
add(2,2)
add(3,2)
