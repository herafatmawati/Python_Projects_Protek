#Program Hapus Tambah Tampilkan Data Sayur

print('Tambah Hapus Data Sayur')
print('-------------------------------------------------------')
sayur=['Bayam','Kangkung','Wortel','Selada']
print('Sayur dalam list: ',sayur)
print('-------------------------------------------------------')
print('Menu:')
print('A.Tambah data sayur')
print('B.Hapus data sayur')
print('C.Tampilkan data sayur')
print()
jawab=str(input('Pilihan Anda: '))
if jawab =='A'or'a':
    tambah=str(input('Masukkan sayur yang akan ditambahkan: '))
    sayur.append(tambah)
    print('Data Sayur setelah ditambahkan: ',sayur)
elif jawab=='B'or'b':
    hapus=str(input('Masukkan nama sayur yang akan dihapus: '))
    sayur.remove[hapus]
    print('Data Sayur setelah dihapus',sayur)
elif jawab=='C'or'c':
    print('Tampilkan semua Sayur yang ada: ',sayur)
