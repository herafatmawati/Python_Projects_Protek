#program membuat bintang bentuk segitiga sama kaki sesuai n dengan function

string=""
n=int(input('Masukkan nilai n= '))
baris=n
def bintang(n):
    for i in range(n):
        print(('*'*(1+2*i)).center(1+2*n))
bintang(n)
        
        
