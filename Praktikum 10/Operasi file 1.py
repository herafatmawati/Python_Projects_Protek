#program membaca file.txt
#tampil banyak bilangan genap dan ganjil


fileku=input('Masukkan nama file : ')
baca=open(fileku,'r')
tampil=baca.readlines()
count=0
itung=0
for i in tampil:
    print(i)
for g in range(len(tampil)):
    if (int(tampil[g])%2)==0:
        count+=1       
    if (int(tampil[g])%2)!=0:
        itung+=1
print('Banyaknya bilangan genap : ',count)
print('Banyaknya bilangan ganjil: ',itung)
baca.close()
    
