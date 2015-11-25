from db import *
tmp=[]
for n in data() :
    tmp.extend(n[11:])

numbers=set(tmp)
print(numbers,"\n\nIt has pulled different numbers: ",len(numbers), ".\n\n")

frequent_numbers={}
for n in data():
    i=11
    while i<16:
        if str(n[i]) in frequent_numbers:
            frequent_numbers[str(n[i])]+=1
        else:
            frequent_numbers[str(n[i])]=1
        i+=1

sorted_list = [(k,v) for v,k in sorted([(v,k) for k,v in frequent_numbers.items()],reverse=True)]
print(sorted_list)
