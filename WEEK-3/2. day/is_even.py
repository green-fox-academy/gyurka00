def is_even(number):
    if number%2==0:
        return("even")
    else:
        return("odd")
number=input("write a number:")
print(is_even(int(number)))
