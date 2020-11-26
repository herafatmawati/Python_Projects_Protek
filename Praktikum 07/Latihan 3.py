print('--------------------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('--------------------------------------')

data=[]
sum=0
i=0
try:
    angka=int(input('Masukkan bilangan bulat: '))
except ValueError:
    print('Bukan bilangan bulat')
jawab=str(input('Lagi(y/n): '))
while jawab == 'y' :
    try:
        angka=int(input('Masukkan bilangan bulat: '))
    except ValueError:
        print('Bukan bilangan bulat')
        angka=int(input('Masukkan bilangan bulat: '))
    jawab=str(input('Lagi(y/n): '))
if jawab == 'n' :
    i += 1
    for angka in data:
        sum += angka
    rerata=sum/i
    print('Rata- ratanya adalah: ',rerata)

