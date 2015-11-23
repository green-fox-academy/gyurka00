def number_convert(get):
    tmp=""
    number=int(get)
    if number//1000 > 0:
        if number//1000==3:
            tmp+="MMM"
            number-=3000
        elif number//1000==2:
            tmp+="MM"
            number-=2000
        else:
            tmp+="M"
            number-=1000
    if number//100>0:
        if number//100==9:
            tmp+="CM"
            number-=900
        elif number//100==8:
            tmp+="DCCC"
            number-=800
        elif number//100==7:
            tmp+="DCC"
            number-=700
        elif number//100==6:
            tmp+="DC"
            number-=600
        elif number//100==5:
            tmp+="D"
            number-=500
        elif number//100==4:
            tmp+="CD"
            number-=400
        elif number//100==3:
            tmp+="CCC"
            number-=300
        elif number//100==2:
            tmp+="CC"
            number-=200
        elif number//100==1:
            tmp+="C"
            number-=100
    if number//10>0:
        if number//10==9:
            tmp+="XC"
            number-=90
        elif number//10==8:
            tmp+="LXXX"
            number-=80
        elif number//10==7:
            tmp+="LXX"
            number-=70
        elif number//10==6:
            tmp+="LX"
            number-=60
        elif number//10==5:
            tmp+="L"
            number-=50
        elif number//10==4:
            tmp+="XL"
            number-=40
        elif number//10==3:
            tmp+="XXX"
            number-=30
        elif number//10==2:
            tmp+="XX"
            number-=20
        elif number//10==1:
            tmp+="X"
            number-=10
    if number//10<10:
        if number//9==1:
            tmp+="IX"
            number-=9
        elif number//8==1:
            tmp+="VIII"
            number-=8
        elif number//7==1:
            tmp+="VII"
            number-=7
        elif number//6==1:
            tmp+="VI"
            number-=6
        elif number//5==1:
            tmp+="V"
            number-=5
        elif number//4==1:
            tmp+="IV"
            number-=4
        elif number//3==1:
            tmp+="III"
            number-=3
        elif number//2==1:
            tmp+="II"
            number-=2
        else:
            tmp+="I"
            number-=1
    return tmp






number=input("Write a number and press enter:")
if int(number)>3999 or int(number)==0:
    print("You are stupid!")
else:
    print(number_convert(number))
