numbers=[1,2,3,4]
output=[]
def even(numbers):
    output=[]
    for n in numbers:
        if n % 2 ==0:
            output.append(n)
    return output

output=even(numbers)
print (output)
