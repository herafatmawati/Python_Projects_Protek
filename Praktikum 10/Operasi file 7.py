#program deskripsi sandi caesar

file=input('Masukkan nama file hasil enkripsi: ')
baca=open(file,'r')
teks=baca.readlines()
asli=''.join(teks)
n=int(input('Masukkan keyword n: '))
hasil=[]
dekripsi=''
for kar in asli:
    if kar.isupper():
        kar_unicode=ord(kar)
        kar_index=ord(kar)-ord('A')
        index_baru=(kar_index-n)%26
        unicode_baru=index_baru+ord('A')
        kar_baru=chr(unicode_baru)
        dekripsi+=kar_baru
    else:
        dekripsi+=kar
hasil.append(dekripsi)
print('Teks asli: ',dekripsi)
filesandi=open('d:\\teksasli.txt','w')
for h in range(len(hasil)):
    filesandi.write(str(hasil[h]))
filesandi.close()                    
baca.close()
