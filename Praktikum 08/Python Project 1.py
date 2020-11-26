#Program Mengurutkan n Bilangan yang diinputkan

print('Mengurutkan n Bilangan yang Diinputkan')
print('--------------------------------------')

n=int(input('Masukkan banyak data yang akan diinputkan: '))
print()
datainput=[]
jumlah=0
i=1
for i in range(0,n):
    print('Masukkan data ke-',str(i+1),':')
    bil=int(input())
    datainput.append(bil)
    datainput.sort(reverse=True)
print('Urutan bilangan secara descending: ')
print(datainput)


