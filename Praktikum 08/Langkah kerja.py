a=[1,5,6,3,6,9,11,20,12]
b=[7,4,5,6,7,1,12,5,9]
a.insert(3,10) #menyisipkan nilai 10 ke dalam indeks ke-3 dari a
b.insert(2,15) #menyisipkan nilai 15 ke dalam indeks ke-2 dari b
a.insert(10,4) #menyisipkan nilai 4 ke dalam indeks terakhir dari a
b.insert(10,8) #menyisipkan nilai 8 ke dalam indeks terakhir dari b
a.sort() #sorting list a secara ascending
b.sort()#sorting list b secara ascending
print('a=',a) #cetak list a
print('b=',b) #cetak list b

c=a[0:8] #mendefinisikan nilai list c = list a dari indeks 0-7
d=b[2:10]#mendefinisikan nilai list d = list b dari indeks 2-9
print('c=',c)
print('d=',d)
print()

c=[1,3,4,5,6,6,9,10]
d=[5,5,6,7,7,8,9,12]

for x in range(0,len(c)):
    print(c[x]+d[x],end=' ')  
print()

e=[6,8,10,12,13,14,18,22]
print('e=',e)
    
ubahtuple=tuple(e)
print('Ubah list e ke tuple e=',ubahtuple)

print('Nilai minimal tuple e= ',min(ubahtuple))
print('Nilai maksimal tuple e= ',max(ubahtuple))
print('Jumlah seluruh elemen tuple e= ',sum(ubahtuple))

myString= 'python adalah bahasa pemrograman yang menyenangkan'
huruf=set(myString)
print('Set myString = ')
print(huruf)
ubahlist=list(huruf)
print('List myString= ')
print(ubahlist)
ubahlist.sort()
print('Urutan myString= ')
print(ubahlist)
