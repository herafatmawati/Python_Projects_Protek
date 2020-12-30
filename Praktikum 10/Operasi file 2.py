#program membaca input berupa: nim,nama mhs,alamat. dan simpan di file txt
#dengan format: nim|nama|alamat

nim=input('Masukkan NIM\t\t:' )
nama=input(str('Masukkan Nama Mhs\t:' ))
almt=input('Masukkan Alamat\t\t:' )
print()
pilih=input('Ulangi inputlagi(y/n)\t:' )
print()
fileku=open('d:\datamahasiswa.txt','w')
teks='{}|{}|{}\n'.format(nim,nama,almt)
fileku.write(teks)
while True:
    if pilih =='y':
        nim=input('Masukkan NIM\t\t:' )
        nama=input(str('Masukkan Nama Mhs\t:' ))
        almt=input('Masukkan Alamat\t\t:' )
        print()
        pilih=input('Ulangi inputlagi(y/n)\t:' )
        print()
        teks='{}|{}|{}\n'.format(nim,nama,almt)
        fileku=open('d:\datamahasiswa.txt','a')
        fileku.write(teks)
    if pilih == 'n':    
        break
fileku.close()
