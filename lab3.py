def a():
    n=int(input("введите количество слов"))
    a=''
    for i in range(n):
        x=str(input("введите слово"))
        a=a+x+" "
    print(a)

a()

def b():
    a=''
    x = str(input("введите слово"))
    while x!='stop':
        a = a + x + " "
        x = str(input("введите слово"))
    print(a)

b()

def c():
    x = str(input("введите слово"))
    if x.count("ф")>0:
        print('вау редкое слово')
    else:
        print('блин слово не редкое')

c()

def d():
    from random import randint

    x=0
    while x<3:
        a=int(randint(0,20))
        b=int(randint(0,20))
        print(a,"+",b,"=")
        y=int(input("введите ответ"))
        if a+b!=y:
            x=x+1
    if x==3:
        print('игра окончена')

d()