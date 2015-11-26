numbers_in=[1,2,3,4]

def reverse_list(list):
    i=len(list)-1
    outpute_list = []
    while i >= 0:
        outpute_list.append(list[i])
        i-=1
    return outpute_list

print(reverse_list(numbers_in))
