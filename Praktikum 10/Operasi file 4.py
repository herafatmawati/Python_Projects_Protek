#program membaca file datamahasiswa.txt
#cari data berdasar nim

cari=input('Masukkan NIM yang mau dicari: ')
fileku=open('d:\datamahasiswa.txt','r')
baca=fileku.read().splitlines()
for i in baca:
    g=i.split('|')
    if cari==g[0]:
        print('Data Mahasiswa')
        print('NIM   :',g[0],'\nNama  :',g[1],'\nAlamat:',g[2])
    if cari!=g[0]:
        cari =='takada'
if cari=='takada':
    print('Data mahasiswa tidak ditemukan')
fileku.close()

