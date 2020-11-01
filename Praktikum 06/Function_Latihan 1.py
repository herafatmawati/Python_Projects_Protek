def isPythagoras(a,b,c):
    a=a**2
    b=b**2
    c=c**2
    jumlah=a+b
    if jumlah==c :
        print('->True')
    else:
        print('->False')

a=3
b=4
c=5
isPythagoras(a,b,c)

a=5
b=9
c=12
isPythagoras(a,b,c)

a=8
b=6
c=10
isPythagoras(a,b,c)

a=7
b=8
c=11
isPythagoras(a,b,c)
