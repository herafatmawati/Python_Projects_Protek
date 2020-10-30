from random import randint
hitung=0
while True:
    hitung += 1
    bil=randint(0,10)
    print(bil)
    if bil == 5:
        break
print('Jumlah perulangan : ',str(hitung))
