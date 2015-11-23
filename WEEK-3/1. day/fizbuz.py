number=input("adj meg egy szzamot: ")
tmp=""
n=0
while n < (int(number)+1):
    if (n%3==0 and n%5==0 and n!=0) or ("5" in str(n) and "3" in str(n)) or ("5" in str(n) and n%3==0) or (n%5==0 and "3" in str(n)):
        print ("fizzbuzz")
    elif n%3==0 and n!=0:
        print ("fizz")
    elif n%5==0 and n!=0:
        print("buzz")
    elif "5" in str(n):
        print("buzz")
    elif "3" in str(n):
        print("fizz")
    else:
        print(n)
    n+=1
