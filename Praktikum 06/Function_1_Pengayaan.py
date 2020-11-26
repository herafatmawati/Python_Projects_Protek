#menentukan bilangan prima dengan fungsi
x=int(input('Masukkan Bilangan: '))
def isPrime(x):
    if x>1:
        for i in range(2,x):
            if (x%i) ==0:
                print(x, 'Bukan bilangan Prima')
                break
        else:
            print(x,'Bilangan Prima')
    else:
        print(x, 'Bukan Bilangan Prima')

isPrime(x)
