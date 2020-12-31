#program cari data peminjaman buku "data peminjaman.txt" berdasar kode member

from datetime import*
cari=input('Masukkan Kode Member  : ')
print()
datapinjam=open('d:\data peminjaman.txt','r')
baca=datapinjam.read().splitlines()
tglkembali=datetime.date(datetime.now())

for data in baca:
    datum=data.split('|')
    denda=2000
    y=datum[3].split('-')
    tglpinjam=date(year=int(y[0]),month=int(y[1]),day=int(y[2]))
    lambat=tglkembali-tglpinjam
    jmldenda=lambat.days*denda
    if cari==datum[0]:
        print('Data Peminjaman Buku')
        print('Kode Member\t\t : ',datum[0],'\nNama Member\t\t : ',datum[1],'\nJudul Buku\t\t : ',datum[2],
              '\nTanggal Mulai Peminjaman : ',datum[3],'\nTanggal Maks Peminjaman  : ',datum[4])
        print('Tanggal Pengembalian     : ',tglkembali,'\nTerlambat\t\t : ',lambat,'hari','\nDenda\t\t\t :  Rp',jmldenda)
        
    if cari!=datum[0]:
        cari=='tak ada'
if cari=='tak ada':
    print('Tidak ada data peminjaman dari Member',cari)
datapinjam.close()
