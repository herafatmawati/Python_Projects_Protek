#program tampilkan bilangan ganjil 1-100
#banyaknya perulangan
sum=0
for i in range(100):
    if (i+1) % 2 ==1:
        print(i+1)
        sum=sum+1
print('Banyaknya Bilangan Ganjil : ',str(sum))

