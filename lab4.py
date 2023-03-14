def zd1():
    x=int(input('введите число'))
    if x%3==0:
        print('делится')
    else:
        print('не делится')

zd1()

def zd2():
    def dl(t):
        return t/100
    x=str(input('введите число'))
    if x.isdigit()==True:
        x=int(x)
        print(dl(x))
    else:
        x=input('введите другое число')

zd2()

def zd3():
    x=str(input('введите дату'))
    a=int(x[:2])
    b=int(x[3:5])
    c=int(x[8:])
    if a*b==c:
        print('год счастливый')
    else:
        print('год не счастливый')


zd3()

def zd4():
    x=str(input('введите номер'))
    k=0
    for i in x:
        k=k+1
    k=k//2
    s1=0
    s2=0
    for i in range (0,k):
        s1=s1+int(x[i])
    for i in range (k,len(x)):
        s2=s2+int(x[i])
    if s1==s2:
        print('билет счастливый')
    else:
        print('не счастливый')

zd4()