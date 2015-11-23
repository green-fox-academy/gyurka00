number=input("adj meg egy szamot: ")
tmp=int(number)
n=2
flag=0
while n<= tmp**0.5:
    if tmp%n==0:
        flag+=1
        break
    n+=1
if flag>0:
    print(tmp,"a szam nem prim")
else:
    print(tmp,"a szam prim")


number=input("\n adj meg egy szamot: ")
tmp=int(number)
print("\n A prim szamok", tmp,"-ig")

i=1
while i < tmp+1:
    flag2=0
    n=2
    while n<= i**0.5:
        if i%n==0:
            flag2+=1
            break
        n+=1
    if flag2==0:
        print(i)
    i+=1
