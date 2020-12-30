#program enkripsi sandi caesar

file=input('Masukkan nama file teks asli: ')
baca=open(file,'r')
teks=baca.readlines()
asli=''.join(teks)
n=int(input('Masukkan keyword n: '))
hasil=[]
enkripsi=''
for kar in asli:
    if kar.isupper():
        kar_unicode=ord(kar)
        kar_index=ord(kar)-ord('A')
        index_baru=(kar_index+n)%26
        unicode_baru=index_baru+ord('A')
        kar_baru=chr(unicode_baru)
        enkripsi+=kar_baru
    else:
        enkripsi+=kar
hasil.append(enkripsi)
print('Teks sandi: ',enkripsi)
filesandi=open('d:\\filesandi.txt','w')
for h in range(len(hasil)):
    filesandi.write(str(hasil[h]))
filesandi.close()                    
baca.close()

