def faktorial(n):
    if n==1:
        return 1
    elif n == 0:
        return 1
    else:
        return(n*faktorial(n-1))
    
n=5
fak1=faktorial(n)
n=3
fak2=faktorial(n)
n=5-3
fak3=faktorial(n)
kombinasi=fak1/(fak2*(fak3))
print('a. C(5,3) : ',kombinasi)

n=10
faktorial1=faktorial(n)
n=10-7
faktorial2=faktorial(n)
permutasi=faktorial1/faktorial2
print('b. P(10,7) : ',permutasi)


    
