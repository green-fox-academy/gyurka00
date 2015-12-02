from moduls.reverse import reverse_list
import os

print(os.getpid())
print(os.getcwd())
print(reverse_list([3,4,5]))


fruit_file = open ('fruits.txt','w')
#print(fruit_file.read())
fruit_file.write('peach')
fruit_file.close()
