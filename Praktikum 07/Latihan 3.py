print('--------------------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('--------------------------------------')

data=[]
i=0

try:
    angka=int(input('Masukkan bilangan bulat: '))
    data.append(angka)
    i += 1
except ValueError:
    print('Bukan bilangan bulat')
    
jawab=str(input('Lagi(y/n): '))
while jawab == 'y' :
    try:
        angka=int(input('Masukkan bilangan bulat: '))
        data.append(angka)
        i += 1
    except ValueError:
        print('Bukan bilangan bulat')
        angka=int(input('Masukkan bilangan bulat: '))
        data.append(angka)
    jawab=str(input('Lagi(y/n): '))
if jawab == 'n' :
    sum=0
    for i in range(len(data)):
        sum += data[i]
    rerata=sum/len(data)
    print('Rata- ratanya adalah: ',rerata)

