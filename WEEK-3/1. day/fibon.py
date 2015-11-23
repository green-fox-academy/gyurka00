number=input("adj meg egy szamot: ")
a=0
b=1
print("0")
print("1")
n=2
while n <= int(number):
    tmp=a+b
    print(tmp)
    a=b
    b=tmp
    n+=1
