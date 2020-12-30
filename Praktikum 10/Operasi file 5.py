#program membaca serangkaian data file txt berisi bilangan
#format: bil1|bil2
#outputnya hasil jumlah bil1 dan bil2

fileku=input('Masukkan nama file : ')
hasil=[]
baca=open(fileku,'r')
tampil=baca.read().splitlines()
for i in tampil:
    a=i.split('|')
    jum=int(a[0])+ int(a[1])
    hasil.append(jum)
    print(jum)
file2=open('d:\\hasilsum.txt','w')
for h in range(len(hasil)):
    file2.write(str(hasil[h])+'\n')
file2.close()
baca.close()

    


