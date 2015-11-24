from db import *
tmp=[]
for n in data() :
    tmp.extend(n[11:])

#print (tmp)
numbers=set(tmp)
print(numbers,"\n\nEddig osszesen ",len(numbers), " kulonbozo szam volt kihuzva.\n\n")

frequent_numbers={}
for n in data():
    i=11
    while i<16:
        if str(n[i]) in frequent_numbers:
            frequent_numbers[str(n[i])]+=1
        else:
            frequent_numbers[str(n[i])]=1
        i+=1
#print (frequent_numbers)

sorted_list = [(k,v) for v,k in sorted([(v,k) for k,v in frequent_numbers.items()],reverse=True)]
print(sorted_list)

"""tel={}
if 'a' in tel:
    tel['a']+=1
else:
    tel['a']=1
print(tel)"""
