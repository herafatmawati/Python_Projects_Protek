#Program hitung gaji karyawan modif

kode=int(input('Masukkan kode karyawan               : '))
nama= str(input('Masukkan nama karyawan               : '))
gol= input('Masukkan golongan                    : ')
status= int(input('Masukkan status [1:menikah/2:belum]  : '))
if status == 1:
    anak=int(input('Masukkan jumlah anak                 : '))
print(':::::::::::::::::::::::::::::::')
print('STRUK RINCIAN GAJI KARYAWAN')
print('...............................')
print('')
print('Nama Karyawan          : ',nama, ' (Kode: ',kode,')')
print('Golongan               : ',gol)
if status ==1:
    print('Jumlah anak adalah     : ',anak)
print('................................')
if gol =='A':
    print('Gaji Pokok             : Rp 10.000.000')
    if status == 1:
        tunjanganSI = 10/100*10000000
        print('Tunjangan Istri/Suami  : Rp ',tunjanganSI)
        tunjanganA = 5/100*10000000*anak
        print('Tunjangan anak         : Rp ',tunjanganA)
        print('...............................')
        upah= 10000000
        kotor= upah+tunjanganSI+tunjanganA
        print('Gaji Kotor            : ',kotor)
        potongan = 10000000*2.5/100
        print('Potongan (2.5%)        : ',potongan)
        gaji= kotor-potongan
        print('...............................')
        print('Gaji Bersih            : Rp ',gaji)
    if status ==2 :
        upah=10000000
        potongan= 10000000*2.5/100
        print('Potongan (2.5%)          : ',potongan)
        gaji= upah - potongan
        print('...............................')
        print('Gaji Bersih            : Rp ',gaji)
elif gol=='B':
    print('Gaji Pokok            : Rp 8.500.000')
    if status == 1:
        tunjanganSI = 10/100*8500000
        print('Tunjangan Istri/Suami  : Rp ',tunjanganSI)
        tunjanganA = 5/100*8500000*anak
        print('Tunjangan anak         : Rp ',tunjanganA)
        print('...............................')
        upah= 8500000
        kotor= upah+tunjanganSI+tunjanganA
        print('Gaji Kotor            : ',kotor)
        potongan = upah*2/100
        print('Potongan (2.0%)        : ',potongan)
        gaji= kotor-potongan
        print('...............................')
        print('Gaji Bersih            : Rp ',gaji)
    if status ==2:
        upah=8500000
        potongan= 8500000*2/100
        print('Potongan (2.0%)         : ',potongan)
        gaji= upah - potongan
        print('...............................')
        print('Gaji Bersih            : Rp ',gaji)
elif gol=='C':
    print('Gaji Pokok             : Rp 7.000.000')
    if status == 1:
        tunjanganSI = 10/100*7000000
        print('Tunjangan Istri/Suami  : Rp ',tunjanganSI)
        tunjanganA = 5/100*7000000*anak
        print('Tunjangan anak         : Rp ',tunjanganA)
        print('...............................')
        upah= 7000000
        kotor= upah+tunjanganSI+tunjanganA
        print('Gaji Kotor                : ',kotor)
        potongan = upah*1.5/100
        print('Potongan (1.5%)        : ',potongan)
        gaji= kotor-potongan
        print('...............................')
        print('Gaji Bersih            : Rp ',gaji)
    if status ==2:
        upah=7000000
        potongan= 7000000*1.5/100
        print('Potongan (1.5%)        : ',potongan)
        gaji= upah - potongan
        print('...............................')
        print('Gaji Bersih            : Rp ',gaji)
elif gol=='D':
    print('Gaji Pokok            : Rp 5.500.000')
    if status == 1:
        tunjanganSI = 10/100*5500000
        print('Tunjangan Istri/Suami  : Rp ',tunjanganSI)
        tunjanganA = 5/100*5500000*anak
        print('Tunjangan anak         : Rp ',tunjanganA)
        print('...............................')
        upah= 5500000
        kotor= upah+tunjanganSI+tunjanganA
        print('Gaji Kotor             : ',kotor)
        potongan = upah*1/100
        print('Potongan (1.0%)        : ',potongan)
        gaji= kotor-potongan
        print('...............................')
        print('Gaji Bersih            : Rp ',gaji)
    if status ==2:
        upah=5500000
        potongan= 5500000*1/100
        print('Potongan (1.0%)         : ',potongan)
        gaji= upah - potongan
        print('...............................')
        print('Gaji Bersih            : Rp ',gaji)
else:
    print('Tidak termasuk dalam golongan')


