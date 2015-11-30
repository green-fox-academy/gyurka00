number = 6

def factor(num):
    out=1
    i = 1
    while i <= number:
        out *= i
        i += 1
    return out

print(factor(number))


def factor2(num):
    if num == 1:
        return 1
    else:
        return factor2(num-1)*num

print(factor2(6))
