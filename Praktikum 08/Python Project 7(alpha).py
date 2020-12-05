#Function untuk menampilkan nama buah dgn harga termahal dari dictionary buah

def tampildict(buah):
    for k in buah:
        urut=list(buah.values())
        urut.sort(reverse=True)
    if urut[0]== 8500:
        print('Buah dengan harga satuan termahal adalah : jeruk')
    elif urut[0]==7800:
        print('Buah dengan harga satuan termahal adalah : mangga')
    elif urut==6500:
        print('Buah dengan harga satuan termahal adalah : duku')
    else:
        print('Buah dengan harga satuan termahal adalah : apel')
    
buah={'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}
tampildict(buah)

