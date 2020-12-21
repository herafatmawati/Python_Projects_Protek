#program modifikasi membuat bintang bentuk segitiga sama kaki sesuai n(harus ganjil) dengan function

string=""
n=int(input('Masukkan nilai n(bil.ganjil)= '))
baris=n
def bintang(n):
    for i in range(n):
        if i<=(n/2):
            print(('*'*(1+2*i)).center(1+2*n))
        else:
            y=0
            print(('*'*(1*y)+'*'*(n-i)+'*'*(n-(i+1))).center(1+2*n))
            y=y+1
            
bintang(n)
        
