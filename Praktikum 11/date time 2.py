#program simpan data peminjaman buku "data peminjaman.txt"

from datetime import*
kode=input('Masukkan Kode Member  : ')
nama=input(str('Masukkan Nama Member  : '))
judul=input('Masukkan Judul Buku   : ')
tglpinjam=datetime.date(datetime.now())
tglkembali=tglpinjam+timedelta(days=7)
print()
pilih=input('Ulangi lagi (y/n)     : ')
print()
datapinjam=open('d:\data peminjaman.txt','w')
isi='{}|{}|{}|{}|{}\n'.format(kode,nama,judul,tglpinjam,tglkembali)
datapinjam.write(isi)
while True:
    if pilih =='y':
        kode=input('Masukkan Kode Member  : ')
        nama=input(str('Masukkan Nama Member  : '))
        judul=input('Masukkan Judul Buku   : ')
        tglpinjam=datetime.date(datetime.now())
        tglkembali=tglpinjam+timedelta(days=7)
        print()
        pilih=input('Ulangi lagi (y/n)     : ')
        print()
        isi='{}|{}|{}|{}|{}\n'.format(kode,nama,judul,tglpinjam,tglkembali)
        datapinjam=open('d:\data peminjaman.txt','a')
        datapinjam.write(isi)
    if pilih=='n':
        break
datapinjam.close()
