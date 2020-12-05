#Program Mengurutkan Nama Mahasiswa dan Menampilkan Jumlah Karakternya
n=int(input('Masukkan banyak nama mahasiswa yang akan diinputkan: '))
print()
Mhs=[]
i=1

for i in range(n):
    print('Masukkan Nama Mahasiswa ',str(i+1),':')
    m=str(input())
    Mhs.append(m)
    Mhs.sort()
    x=list(map(lambda m:len(m),Mhs))
    ubah=tuple(Mhs)
print(Mhs,x)



    
