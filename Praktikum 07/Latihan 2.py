namafile=input('Masukkan nama file: ')
file=open('namafile','a')
try:
teks=input('Data yang mau ditambahkan: ')
file.write(teks)
jawab=str(input('Mau lagi(y/n): '))
while jawab == 'y' :
    teks=input('Data yang mau ditambahkan: ')
    jawab=str(input('Mau lagi(y/n): '))
if jawab == 'n' :
    file.close()
except:
    print('Masukkan data dengan benar')
