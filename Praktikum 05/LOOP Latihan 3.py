#program tampilkan bilangan ganjil 1-100
#banyaknya perulangan
#jumlah semua bilangan
sum=0
total=0
for i in range(100):
    if (i+1) % 2 ==1:
        print(i+1)
        sum=sum+1
        total=total+(i+1)
print('Banyaknya Bilangan Ganjil : ',str(sum))
print('Hasil penjumlahan',str(sum),'bilangan ganjil 1-100 adalah',str(total))
