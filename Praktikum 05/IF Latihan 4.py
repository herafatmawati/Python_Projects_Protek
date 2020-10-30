kode=int(input('Masukkan kode karyawan : '))
nama= str(input('Masukkan nama karyawan : '))
gol= input('Masukkan golongan      : ')

print(':::::::::::::::::::::::::::::::')
print('STRUK RINCIAN GAJI KARYAWAN')
print('...............................')
print('')
print('Nama Karyawan          : ',nama, ' (Kode: ',kode,')')
print('Golongan               : ',gol)
print('................................')
if gol =='A':
    print('Gaji Pokok             : Rp 10.000.000')
    upah= 10000000
    potongan = 10000000*2.5/100
    print('Potongan (2.5%)        : ',potongan)
    gaji= upah - potongan
    print('...............................')
    print('Gaji Bersih            : Rp ',gaji)
elif gol=='B':
    print('Gaji Pokok              : Rp 8.500.000')
    upah=8500000
    potongan= 8500000*2/100
    print('Potongan (2.0%)         : ',potongan)
    gaji= upah - potongan
    print('...............................')
    print('Gaji Bersih            : Rp ',gaji)
elif gol=='C':
    print('Gaji Pokok              : Rp 7.000.000')
    upah=7000000
    potongan= 7000000*1.5/100
    print('Potongan (1.5%)        : ',potongan)
    gaji= upah - potongan
    print('...............................')
    print('Gaji Bersih            : Rp ',gaji)
elif gol=='D':
    print('Gaji Pokok              : Rp 5.500.000')
    upah=5500000
    potongan= 5500000*1/100
    print('Potongan (1.0%)         : ',potongan)
    gaji= upah - potongan
    print('...............................')
    print('Gaji Bersih            : Rp ',gaji)
else:
    print('Tidak termasuk dalam golongan')
